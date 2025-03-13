import streamlit as st

# --- Custom CSS for colors ---
st.markdown("""
<style>
    .skill {
        color: #32CD32; /* Lime green color */
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)



# CSS for consistent styling of all bullet points in a section
st.markdown("""
<style>
    .styled-bullet-points {
        margin-left: 0px; /* Adjusts indentation for the entire block */
        padding-left: 0px; /* Adds spacing inside the block */
        text-indent: -20px;
        line-height: 1.6; /* Increases line spacing for better readability */
    }
</style>
""", unsafe_allow_html=True)



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("views/i/work_pic_2025.jpg", width=230)

with col2:
    st.title("Rick", anchor=False)
    st.write(
        "Lead Security Analyst&nbsp;&nbsp;&nbsp; || &nbsp;&nbsp;&nbsp;Lead Security Engineer&nbsp;&nbsp; || &nbsp;&nbsp;&nbsp;Automation Engineer"
    )
    if st.button("Contact Me", key="contact_me_button"):
        st.session_state.show_form = True

# --- EDUCATION ---
st.markdown('## Education', unsafe_allow_html=True)
st.markdown('<div style="margin-bottom: 5px;"><strong>Bachelors of Science</strong> (CIS), <em>Park University</em>, US&nbsp; -&nbsp;&nbsp;2012</div>', unsafe_allow_html=True)
#st.markdown('<div style="margin-bottom: 5px;">2012</div>', unsafe_allow_html=True)

# --- WORK EXPERIENCE ---
st.markdown('## Work Experience', unsafe_allow_html=True)

st.markdown('<div style="margin-bottom: 5px;"><strong>Senior Security Analyst - IBM</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points = [
    "Utilized QRadar (SIEM) to monitor, detect, research, and respond to diverse incident alerts, advancing time-to-resolution thus ensuring swift threat mitigation",
    "In-depth investigations using CrowdStrike, Microsoft Defender, and Uptycs (CNAPP), successfully remediating vulnerabilities and enhancing cyber security posture",
    "Provided forensic analysis across Windows, Linux, and Mac systems to support incident investigations and containment efforts",
    "Performed advanced confirmation and insights on complex alerts, addressing identification of risks, threats, and correlating with MITRE ATT&CK TTPs",
    "Aided rule tuning team for false positive alerts, refining detection signatures for cloud environments dividing legitimate from malicious code compilation activities",
    "Doubled as red-team to disprove false-positive OWASP Top 10 incidents, debunking suspected malicious activities and ensuring accurate threat assessments",
    "Discovered new crypt mining activity in Kubernetes cloud cluster via Uptycs web console executing CLI tools halting harmful actions",
    "Added custom, actionable threat intelligence to external threats, IOC's, and sandbox analysis, delivering readable and useful insights to stakeholders",
    "Developed automation scripts extracting internal user and hardware inventory data from IBM’s non-Active Directory databases reducing ticket time-to-resolution"
]
###newest way
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)





st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20






st.markdown('<div style="margin-bottom: 5px;"><strong>Lead Security Engineer - Prudential</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_1 = [
    "Engineered advanced integrations across Google Apigee, Splunk Cloud SOAR, and Bitbucket API securing on-premises-to-cloud data exchanges and high-volume workflows",
    "Managed AWS, Azure, and Splunk cloud environments, optimizing data retrieval pipelines, aggregating telemetry, and enhancing data-driven decision-making through seamless orchestration of cloud-native tools and automated processes",
    "Orchestrated the integration of IBM Resilient and Splunk SIEM platforms, propelling automated ticket workflows",
    "Directed the interpretation, design, and implementation of security compliance controls, adhering to NIST standards. "
    "Created custom dashboards, particularly generating rapid insights for audit/risk team facilitating real-time compliance tracking and audit readiness",
    "Leveraged extensive threat-hunting expertise to create comprehensive analyst training materials",
    "Authored digital guides demonstrating practical, detailed instruction for navigating various threat-hunting platforms reducing team transition and familiarization times",
    "Developed Python playbook preserving version control, storage, and recovery of playbook data via BitBucket cloud API ensuring secure, reliable artifact collection and delivery",
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_1])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)


st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20



st.markdown('<div style="margin-bottom: 5px;"><strong>Senior Security Analyst/Automation Engineer - Large Health Agency</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_2 = [
    "Customized advanced integrated threat-hunting investigations across RSA SIEM Suite, FireEye IPS/Sandbox, Palo Alto NGFW, BeyondTrust appliances and API's"
    "Configured data ingestion across Ixia, MS Azure, Tenable, VirusTotal, Cisco, Infoblox, Tanium, and Bit9 plus many more sources",
    "Test and adjust advanced SIEM queries/filters to detect attacks based on IOC's, forensic data, or decoded malicious payloads",
    "Analyzed multi-sourced threat intelligence to deliver actionable IOCs and enrich incident context through RSA ThreatConnect SOAR",
    "Automated phishing and IPS alert response workflows to isolate endpoints and initiate forensic scans during large number events",
    "Applied MITRE ATT&CK, OWASP Top 10 attack signatures to incident response tickets improve management and audit metrics",
    "Enhanced SOC workflows and playbooks delivering enriched analyst pre-populated tickets reducing incident time-to-resolution under two minutes",
    "Leveraged SIEM, FireEye and Palo API's with Python to pass every downloaded executable URLs to FireEye sandbox, enabling rapid threat investigation",
    "Authored video walk-through of response time for user report phishing using Python IOC extraction from phishing emails using REGEX prior to BeyondTrust",
    "Introduced pragmatic screen-recording videos simplifying complex training SOC processes many for SOAR how-to education instruction"
    "Designated department member to participate in agency-wide network attack tabletop exercises"
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_2])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)



st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20



st.markdown('<div style="margin-bottom: 5px;"><strong>Lead SOC Engineer - FICO</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_3 = [
    "Achieved automation of ServiceNow ticket generation for AlienVault agent reinstalls, streamlining ~800 agent deployments across the enterprise via custom-written Python API integration",
    "Developed and deployed remote forensic collection scripts (EXE, bash, and text-based commands), directing local admins on endpoint data retrieval in environments lacking EDR solutions",
    "Independently enabled NetFlow and packet analysis for FICO SOC team bridging network data flows during agent re-install periods or information blackouts",
    "Enhanced overall SOC visibility via API integration of AlienVault SIEM plus additional data sources Logstash, Zabbix, Okta, Qualys, SolarWinds",
    "Spearheaded the initiative to replicate production environments to dev facilitating advanced Proof of Concept (PoC) solutions for various customer departments",
    "Strategically led the integration of multiple appliance APIs establishing a significant leap in endpoint intelligence capabilities for incident response",
    "Engineered the development of a near-real-time SIEM leveraging Security Onion, NetFlow, network packet sensors, Python automation, and Open Source Intelligence (OSINT)",
    "Automated and customized a comprehensive list of open-source threat intelligence, incorporating timed automatic updates, enriching incident tickets, and enhancing SOC readiness capability",
    "Delivered rich presentations of custom SIEM cybersecurity tools to the data science team, translating complex technical concepts into accessible formats"
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_3])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)



st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20




st.markdown('<div style="margin-bottom: 5px;"><strong>Senior Security Engineer (Red Team) - Synack Inc.</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_4 = [
    "Discover and exploit security vulnerabilities in unique client environments via custom Python, Burp Suite and Kali Linux tools sets",
    "Offensively test for weaknesses in policy compliance to confirm/deny suspected vulnerabilities or address customer specific security concerns",
    "Execute working exploits (regression testing) against patched systems, or vulnerability scans across client networks reconsiling weaknesses in network fabric",
    "Validated and replicated advanced red-team submitted exploits requiring the build and deployment of complex test environments confirming exploit impact prior to client delivery",
    "Thoroughly reviewed and verified red-team submitted exploits ensuring adherence to high-quality standards, delivering elite, actionable reports that are clear, precise, and easily followed by clients",
    "Responsible for establishing, correcting, and maintaining clear communications with Synack SRT crowd-sourced community via multi-platform channels aligning their research with client security contracts and concerns",
    "Continually engage in web and host penetration tests for large corporate enterprises reducing client attack surface and providing top-tier vulnerability reports maintaining policy compliance",
    ]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_4])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)



st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20



st.markdown('<div style="margin-bottom: 5px;"><strong>Senior Enterprise Analyst/Engineer - Texas Tech HSC</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_5 = [
    "Deployed and configured Cisco IPS, ASA firewall layered at edge and data center completing campus independence and separation from Lubbock campus"
    "Migrating campus to open-source Central Authentication Service Project (aka IAM) for improved identification during cyber security investigations",
    "Managed CIS benchmark audits and optimized firewall, router, and IPS configurations using AlgoSec, enhancing compliance and eliminating redundant rules"
    "Developed custom Python code for configuration and deployment of McAfee enterprise Data Leakage Prevention (DLP), e-Policy Orchestrator (ePO), disk encryption, Virus Scan, Host Intrusion Prevention (HIPS) applications",
    "Participated in pentest of on-campus law-enforcement networks patching team discovered exploits introducing enhanced FW rule-sets constructing TTUHSC security posture across segmented network",
    "Spearheaded network-wide patch script developed to change remote system registries and default browser settings ensuring GPO compliance remains active",
    "Curated information security training curricula for all new TTUHSC employees, and conducted monthly onboarding InfoSec presentations"
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_5])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)



st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20




st.markdown('<div style="margin-bottom: 5px;"><strong>Network/Security Architect  - Large Gov Contractor/Construction</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_6 = [
    "Re-design network introducing NIST security controls preceded by the implementation of a layered network model",
    "Deployed enterprise-wide GPO's enabling more data collection and log production that necessitate NIST compliance upgrading security and company posture",
    "Designed/tested network recovery practices especially for MS Exchange by virtualizing production servers to containers improving redundancy  for redeployment operations",
    "Introduced endpoint OSSEC agents on systems, employed Security Onion IDS, Untangle UTM, multiple endpoint protection suites escalating network visibility",
    "Conducted pentests against network devices and applications reducing attack surfaces, providing vulnerability tracking data for proactive mitigation strategies",
    "Developed training for information assurance and compliance annual training with remote option via the open-source web training platform Moodle",
    "Coordinated with users, management, and external personnel to conduct compliance audits assuring continued adherence to NIST security controls"
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_6])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)




st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20




st.markdown('<div style="margin-bottom: 5px;"><strong>Information System Security Officer (ISSO)  - USIBWC federal agency</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_7 = [
    "Achieved certification and accreditation for FISMA (NIST) security via total creation and development of all policies, POAMs, ST&Es, threat analysis, and Business Impact Assessments",
    "Developed, prepared, and distributed policy guidance standards for cybersecurity practices, processes, and compliance requirements for any and all network components",
    "Created and developed scripts to perform fully remote administration and automation functions providing removal/reinstall McAfee/Checkpoint EDR suites additionally deploying GPOs lacking a MS Domain Controller",
    "Deployed Enterasys Dragon IDS providing deeper network visibility to conduct investigations into malicious traffic",
    "Functioned as USIBWC representative responding to quarterly and annual POAM and compliance reports for federal OMB office and agency commissioner",
    "Created and managed annual web-based information assurance training for entire agency, including testing and storage of completion certificates for documented FISMA compliance",
    "Configured and managed all Cisco network switching and routing across all HQ and remote offices spread along the U.S/Mexico boarder supporting 9 sites",
    "Developed agency-wide user workstation images configuring security agents in complaince with NIST standards enabling remote reimage/quarantine, GPO and forensic gathering capabilities",
    "Migrated over 5 enterprise servers including email system GroupWise to Suse Linux Enterprise upon Netware phase-out",
    "Configured edge router defining internal/external, DMZ zones deploying Astaro FW (aka Sophos UTM) at network edge bolstering agency security and visibility",
    "Deployed agency wide drive encryption to all issued external network drives and workstations ensuring CIA triad and in further effort to comply with NIST requirements",
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_7])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)




st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20







st.markdown('<div style="margin-bottom: 5px;"><strong>Information Security Specialist  -  DoD Combat Development - THAAD</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_8 = [
    "Deploy and manage combat simulations Windows domain accommodate Red Hat Linux clients for continuous mission training",
    "Perform server and network administration for unclassified networks in addition to IT support services for all department operations personnel",
    "Regular interval patching practices as well as continues adjustment and application of NSA/DISA endpoint security configuration controls"
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_8])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)




st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20







st.markdown('<div style="margin-bottom: 5px;"><strong>Network Administrator  -  Drug Enforcement Administration (DEA contractor)</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_9 = [
    "Provide network administration of Cisco hardware segmenting VLAN's, disable/enable routes to/from remote multi-agency systems",
    "Apply security configurations to traffic via ACL's, port security and continuously perform network best practices",
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_9])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)


st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)###line spacer x20



st.markdown('<div style="margin-bottom: 5px;"><strong>USAF  -  Airman</strong></div>', unsafe_allow_html=True)
# Description bullet points
description_points_9 = [
    "Imagery analyst/Predator UAV sensor operator supporting multi source intelligence collection",
]
###newest way to print
# Create HTML list items
list_items = "".join([f"<li>{point}</li>" for point in description_points_9])
# Display the formatted list
st.markdown(f'<div class="job-description"><ul>{list_items}</ul></div>', unsafe_allow_html=True)


st.markdown('<div style="margin-bottom: 40px;"></div>', unsafe_allow_html=True)###line spacer x20






# --- WRITTEN TOOLS ---
st.markdown('## Written Tools', unsafe_allow_html=True)
st.markdown('<div style="margin-bottom: 5px;"><strong>Linux Boomerang</strong>: add your IPs and CLI commands - this will grab and return output to you while remote.</div>', unsafe_allow_html=True)

# --- SKILLS ---
st.markdown('## Skills', unsafe_allow_html=True)

# Define skills with individual control over spacing
skills = [
    ("Programming:", "Python, Bash"),
    ("Data parsing/processing:", "SQL"),
    ("Deep Learning:", "TensorFlow"),
    ("Web development:", "Flask"),
    ("Model deployment:", "streamlit")
]

# Control each skill's indentation using inline styles
for label, value in skills:
    # Use inline styles to control spacing
    st.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 2px;">'
                 f'<span style="width: 200px; font-weight: bold;">{label}</span>'  # Label with fixed width
                 f'<span class="skill" style="margin-left: 10px;">{value}</span></div>', unsafe_allow_html=True)

