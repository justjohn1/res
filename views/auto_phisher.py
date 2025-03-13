import streamlit as st

# Title and Introduction
st.title("🔍 Automated Phishing & Threat Intelligence Platform")
st.write(
    "**Before BeyondTrust PhishER, my custom-built platform handled phishing email analysis, extracted threat intelligence, "
    "and streamlined security operations. This system automated the SOC workflow for processing user-submitted phishing emails, "
    "analyzing malicious indicators, and generating incident response tickets in RSA Archer.**"
)

st.markdown("---")

# 🎯 Core Capabilities
st.header("🎯 Core Capabilities")
st.markdown("""
- 📨 **Automated Phishing Email Analysis** – Extracts IOCs (Indicators of Compromise) from user-submitted phishing emails.  
- 🔍 **Threat Intelligence Processing** – Parses email contents for URLs, domains, hashes, and suspicious keywords.  
- 🛡️ **Enterprise-Scale Security Integration** – Feeds extracted threats into **RSA Archer**, **FireEye**, and **Microsoft Graph API**.  
- 🚀 **Incident Response Acceleration** – Reduces phishing analysis turnaround from days to minutes.  
- 📊 **Performance Optimization & Monitoring** – Measures email flow, scanning speed, and SOC response times.  
""")

st.markdown("---")

# 📧 Phishing Email Processing
st.header("📧 Phishing Email Processing Workflow")
st.write(
    "**SOC teams manually reviewing user-reported phishing emails slows down security response. "
    "This system automatically extracts phishing indicators and accelerates investigations.**"
)

st.markdown("""
- 📩 **Retrieves Suspect Emails from Exchange** – Pulls **100 latest emails** flagged as phishing by users.  
- 🕵️‍♂️ **Extracts Metadata & Threat Indicators** – Parses sender info, timestamps, and suspicious attachments.  
- 🔗 **Identifies Malicious URLs & Domains** – Uses regex-based URL detection and domain parsing.  
- 🛠 **Hashes & Deduplicates Alerts** – Prevents duplicate processing by hashing email subjects & attachments.  
""")

st.markdown("---")

# 🔎 Threat Intelligence Extraction
st.header("🔎 Threat Intelligence Extraction")
st.write(
    "**Extracted phishing indicators feed into multiple security tools for deeper analysis and automated blocking.**"
)

st.markdown("""
- 🔍 **URLs & Domains Extraction** – Scans email bodies for embedded malicious URLs.  
- 🛡 **Hashes for Threat Attribution** – Generates SHA-256 hashes of email subjects and attachments.  
- 🔥 **FireEye Malware Analysis Submission** – Automatically detonates phishing URLs & attachments in FireEye.  
- 🏴 **Blacklist & Threat Intelligence Feeds** – Compares URLs/domains against known phishing indicators.  
""")

st.markdown("---")

# 🚀 Automated RSA Archer Ticketing
st.header("🚀 Automated RSA Archer Ticketing")
st.write(
    "**Security incidents need structured tracking. This system auto-generates tickets in RSA Archer, linking threat intelligence findings.**"
)

st.markdown("""
- 📋 **Creates Phishing Incident Reports** – Automates ticket generation in RSA Archer.  
- 📌 **Links Threat Intelligence Data** – Connects IOCs (Indicators of Compromise) to security events.  
- 🔄 **Updates Investigation Progress** – Appends journal entries to track analysis workflow.  
""")

st.code("""
payload_2 = '{"Content": {"LevelId": 232, "Tag": "Title", "FieldContents": {"16132": {"Type": 1, "Tag": "Title", "Value": "%s", "FieldId": 16132}, \
    "16108": {"Type": 1, "Tag": "Incident Summary", "Value": "%s", "FieldId": 16108}}}}' % (title_sum, title_sum)
""", language="python")

st.markdown("---")

# 🏗 Scalable Security Workflow
st.header("🏗 Scalable Security Workflow")
st.markdown("""
- 🚀 **SOC-Ready Automation** – Replaces manual triage with fully automated threat processing.  
- 🔄 **Seamless Security Tool Integration** – Connects Microsoft Graph API, RSA Archer, and FireEye.  
- 📊 **Optimized for Enterprise-Scale Operations** – Efficiently processes thousands of phishing reports.  
""")

st.markdown("---")

# ⚡ Performance Optimization
st.header("⚡ Performance Optimization")
st.markdown("""
- ⏳ **Time-Based Execution** – Filters alerts based on recent timestamps to avoid outdated reports.  
- 💾 **Efficient Data Storage** – Uses structured logs & databases to avoid redundant processing.  
- 🏆 **Scalability & Speed** – Processes phishing alerts at high speed, ensuring real-time threat response.  
""")

st.markdown("---")

# 🏆 Why This Project Was Critical
st.header("🏆 Why This Project Was Critical")
st.markdown("""
- 🛡 **Preceded PhishER Deployment** – Provided a **custom-built** phishing response platform before BeyondTrust PhishER.  
- 🚀 **Accelerated Incident Response** – Reduced phishing investigation times from **days to minutes**.  
- 🔍 **Strengthened Threat Intelligence Capabilities** – Extracted IOCs and enriched security data.  
- 📊 **Optimized Security Workflows** – Integrated **FireEye, RSA Archer, and Microsoft Graph API** for automated processing.  
""")

st.markdown(
    "**This system helped SOC teams process phishing reports efficiently, reducing manual effort and improving security operations.**"
)

