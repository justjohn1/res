import streamlit as st
import base64
import requests
import yaml
import re
from datetime import datetime
from pathlib import Path
st.set_option('client.showErrorDetails', False)


# Configuration
b_data = Path(__file__).parent.parent / "b_data"
ACCESS_LOG = b_data / "b_logs.yaml"
METRICS_FILE = b_data / "metrics.yaml"
BLOCKLIST = b_data / "blocklist.yaml"
STATIC_PWD = st.secrets["auth"]["password"]

def _init_files():
    """Ensure required files exist"""
    b_data.mkdir(exist_ok=True)
    for f in [ACCESS_LOG, METRICS_FILE, BLOCKLIST]:
        if not f.exists():
            f.touch()

def _log_attempt(email: str, ip: str, success: bool):
    """Log all access attempts with base64 encoding"""
    timestamp = datetime.now().isoformat()
    log_entry = f"{timestamp}::{email}::{ip}::{success}"
    encoded = base64.b64encode(log_entry.encode()).decode()
    
    # Append to YAML list safely
    existing = []
    if ACCESS_LOG.exists():
        with open(ACCESS_LOG) as f:
            existing = yaml.safe_load(f) or []
    
    existing.append(encoded)
    with open(ACCESS_LOG, "w") as f:
        yaml.dump(existing, f)

def _update_metrics(email: str, ip: str):
    """Update visitor counters and domain tracking"""
    metrics = {"total_visits": 0, "unique_ips": [], "domains": {}}
    
    if METRICS_FILE.exists():
        with open(METRICS_FILE) as f:
            loaded = yaml.safe_load(f) or {}
            metrics.update(loaded)
    
    # Ensure list format for IPs
    if isinstance(metrics.get("unique_ips"), set):
        metrics["unique_ips"] = list(metrics["unique_ips"])
    
    metrics["total_visits"] += 1
    
    # Update IP tracking
    if ip not in metrics["unique_ips"]:
        metrics["unique_ips"].append(ip)
    
    # Update domain tracking
    domain = "unknown"
    if "@" in email:
        domain = email.split("@")[-1].lower()
        metrics["domains"][domain] = metrics["domains"].get(domain, 0) + 1
    
    with open(METRICS_FILE, "w") as f:
        yaml.dump(metrics, f)

def _check_blocklist(ip: str, email: str) -> bool:
    """Check against blocklist (empty list allows all)"""
    if not BLOCKLIST.exists():
        return False
        
    with open(BLOCKLIST) as f:
        blocklist = yaml.safe_load(f) or {}
        
    domain = email.split("@")[-1].lower() if "@" in email else ""
    return any([
        ip in blocklist.get("ips", []),
        email.lower() in blocklist.get("emails", []),
        domain in blocklist.get("domains", [])
    ])

def _validate_email(email: str) -> bool:
    """Block free email providers using regex"""
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    return not any(domain in email.lower() 
                   for domain in ["gmail.com", "yahoo.com", "outlook.com"])

def _get_client_ip() -> str:
    """Get real IP behind Streamlit Cloud proxy"""
    try:
        headers = st.secrets.get("headers", {})
        if "X-Forwarded-For" in headers:
            return headers["X-Forwarded-For"].split(",")[0].strip()
        return requests.get("https://api.ipify.org").text
    except:
        return "unknown"

def enforce_auth():
    """Main authentication gateway without session state conflicts"""
    _init_files()
    
    # Initialize authentication state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.auth_attempts = 0
    
    if not st.session_state.authenticated:
        with st.form(key="auth_form"):
            email = st.text_input("Work Email")
            password = st.text_input("Access Code", type="password")
            submitted = st.form_submit_button("Unlock")
            
            if submitted:
                ip = _get_client_ip()
                blocked = _check_blocklist(ip, email)
                valid_email = _validate_email(email)
                valid_pwd = password == STATIC_PWD
                success = valid_pwd and valid_email and not blocked
                
                # Log attempt
                _log_attempt(email, ip, success)
                _update_metrics(email, ip)
                
                if blocked:
                    st.error("🚫 Access denied - You're blocked")
                elif success:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.session_state.auth_attempts += 1
                    st.error(f"❌ Invalid credentials")
        
        # Stop execution if not authenticated
        st.stop()

