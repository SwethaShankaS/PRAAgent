import streamlit as st
st.set_page_config(page_title="Performance Risk Assessment", layout="wide")
st.markdown(
    """
    <style>
    .stRadio label,
    div[data-testid="stRadio"] label,
    .stRadio > div > label,
    div[data-testid="stRadio"] .stRadio > div > label {
        font-size: 1.3rem !important;
        font-weight: 600;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("🚀 Performance Risk Assessment")

# -------------------------
# SESSION STATE
# -------------------------
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "active_tile" not in st.session_state:
    st.session_state.active_tile = None
# -------------------------
# SECTIONS WITH EXACT QUESTIONS ✅
# -------------------------
sections = {
# -------------------------
# SYSTEM Assessment
# -------------------------
"System Assessment": {
    "icon": "🧪",
    "questions": [
        ("The users of the service internal staff, external customers or both?",
         {"Both":50, "External":40, "Internal":30}),
        ("Is the business service critical?",
         {"Maybe":40, "No":30}),
        ("Have there been any historical performance issues with this service or system?",
         {"Maybe":40, "No":30})
    ]
},
# -------------------------
# PRODUCTION CAPACITY
# -------------------------
"Production Capacity": {
    "icon": "📊",
    "questions": [
        ("What is the current capacity utilisation of the service?",
         {">80%":50, "61-80%":50, "41-60%":30, "21-41%":20, "0-20%":10}),
        ("What is the current annual growth rate?",
         {"50+":50, "25-49%":50, "10-24%":40, "6-9%":30, "5% or less":10}),
        ("Are there any changes in the NFR's?",
         {"Yes":0, "No":0}),
        ("Is the break point of the system known?",
         {"Yes":0, "No":0})
    ]
},
# -------------------------
# SYSTEM CHANGES
# -------------------------
"System changes and availability": {
    "icon": "🔄",
    "questions": [
        ("Version upgrades for open JDK spring boot etc tech upgrade?",
         {"major":0, "minor":0}),
        ("Any existing issues on the tech upgrade or versions",
         {"yes":0, "No":0}),
        ("Does this change introduce new functions or additional capability to existing functions?",
         {"yes":70, "No":30, "Existing App- No change/First Time PNV":20}),
        ("New platform/ service migration?",
         {"yes":80, "No":20}),
        ("Is the change affecting the database or data access patterns?",
         {"yes":80, "No":20}),
        ("Does the change involve significant refactoring or re architecture of the application?",
         {"yes":80, "No":20}),
        ("What type of change is being implemented?",
         {
             "New feature/Implementation":30,
             "Logic or Code Changes":20,
             "Security Patch":15,
             "Infra Change/Upgrade":10,
             "Cosmetic/ Config Change":5
         }),
        ("Changes to Code/Infra?",
         {"Yes":80, "No":20})
    ]
},
# -------------------------
# RESOURCE UTILISATION
# -------------------------
"Resource Utilisation": {
    "icon": "💻",
    "questions": [
        ("What type of infrastructure is the applications running on",
         {"On-Premises":40, "Cloud":40, "Hybrid":30}),
        ("Are there any recent or planned changes to the infrastructure?",
         {"Yes":0, "No":0}),
        ("Is the application using containerization or microservices architecture?",
         {"Yes":0, "No":0})
    ]
},
# -------------------------
# IMPACT FACTORS
# -------------------------
"Impact Factors": {
    "icon": "📈",
    "questions": [
        ("Do you know the current volume metrics of your application?",
         {"Yes":70, "No":30}),
        ("In terms of volume - what are the number of concurrent users",
         {"5000-9999":50, "1000-4999":50, "500-999":40, "100-499":30}),
        ("In terms of volume - what is the anticipated transaction rate (TPH - transactions per hour)?",
         {"15000+":50, "5000+":50, "2000+":50, "500+":40})
    ]
    
},
# -------------------------
# PERFORMANCE & STABILITY
# -------------------------
"Performance & Stability": {
    "icon": "⚙️",
    "questions": [
        ("How scalable is the service to handle increased loads(TPS)?",
         {"Highly Scalable":0, "Moderately Scalable":0, "Limited Scalable":0, "Not Scalable":10}),
        ("How easily can the service or system scale to meet increased demand?",
         {"Moderate Difficult":0, "Somewhat Difficult":0, "Very Difficult":0})
    ]
},
# -------------------------
# COMPLEXITY
# -------------------------
"Complexity": {
    "icon": "🔗",
    "questions": [
        ("Impact on the numbers selected complex an integration partners",
         {"High":0, "Medium":0, "Low":10, "N/A":5})
    ]
},
# -------------------------
# ✅ AI PERFORMANCE & SCALABILITY
# -------------------------
"AI Performance & Scalability": {
    "icon": "🤖",
    "questions": [
        ("Overall pipeline time increase due to AI",
         {">50%":50, "25–50%":40, "10–25%":30, "<10%":10}),
        ("Do security scans using AI affect performance?",
         {"Significant":50, "Moderate":40, "Minimal":30, "Optimized":10}),
        ("Can delays be traced to specific AI/agent components?",
         {"No":50, "Partial":40, "Mostly":20, "Fully traceable":10}),
        ("Impact of third-party AI APIs under load",
         {"High latency":50, "Moderate latency":40, "Low latency":20, "Local/optimized":10}),
        ("Are repeated AI calls optimized via caching?",
         {"No caching":50, "Partial":40, "Effective":20, "Fully optimized":10}),
        ("Do AI steps create bottlenecks in CI/CD?",
         {"Severe":50, "Moderate":40, "Minor":20, "None":10}),
        ("Is auto-scaling enabled for AI workloads?",
         {"No":50, "Manual scaling":40, "Partial auto-scale":20, "Fully automated":10}),
        ("Failure rate of AI steps during volume testing",
         {">10%":50, "5–10%":40, "1–5%":20, "<1%":10}),
        ("P95 latency for AI-driven pipeline stages",
         {">10s":50, "5–10s":40, "2–5s":20, "<2s":10}),
        ("Number of agents tested concurrently in workflows",
         {"1–2":50, "3–5":40, "5–10":20, ">10":10}),
        ("What is the maximum tested prompt/context size?",
         {"<2k tokens":50, "2k–8k tokens":40, "8k–32k tokens":20, ">32k tokens":10}),
        ("Does inter-agent communication impact performance?",
         {"High impact":50, "Moderate":40, "Low":20, "Optimized":10})
    ]
}
}
# -------------------------
# TILE UI
# -------------------------
st.subheader("📂 Select Section")
cols = st.columns(3)
for i, section in enumerate(sections):
    col = cols[i % 3]
    if col.button(f"{sections[section]['icon']} {section}", use_container_width=True):
        st.session_state.active_tile = section
# -------------------------
# SHOW QUESTIONS
# -------------------------
if st.session_state.active_tile:
    section = st.session_state.active_tile
    st.markdown(f"### {sections[section]['icon']} {section}")
    placeholder = "-- Choose your option --"
    for i, (question, options_dict) in enumerate(sections[section]["questions"]):
        key = f"{section}_{i}"
        options = [placeholder] + list(options_dict.keys())
        answer = st.radio(question, options, index=0, key=key)
        if answer != placeholder:
            st.session_state.responses[key] = {
                "answer": answer,
                "score": options_dict[answer]
            }
        elif key in st.session_state.responses:
            del st.session_state.responses[key]
# -------------------------
# SUBMIT
# -------------------------
if st.button("Submit Assessment ✅"):
    total_score = 0
    section_scores = {}
    unanswered_questions = []
    # ✅ CHECK ALL QUESTIONS FIRST
    for section, details in sections.items():
        for i, (question, _) in enumerate(details["questions"]):
            key = f"{section}_{i}"
            if key not in st.session_state.responses:
                unanswered_questions.append(f"{section} → {question}")
    # ✅ IF ANY QUESTION NOT ANSWERED → STOP
    if len(unanswered_questions) > 0:
        st.error("⚠ Please complete ALL questions before submitting.")
        st.stop()
    # ✅ ONLY IF ALL ANSWERED → CALCULATE SCORES
    for section, details in sections.items():
        sec_score = 0
        for i, _ in enumerate(details["questions"]):
            key = f"{section}_{i}"
            response = st.session_state.responses.get(key)
            if response:
                sec_score += response["score"]
                total_score += response["score"]
        section_scores[section] = sec_score
    # ✅ RISK CLASSIFICATION
    if total_score >= 400:
        risk = "HIGH RISK"
    elif total_score >= 200:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"
    # ✅ SAVE
    st.session_state["total_score"] = total_score
    st.session_state["risk"] = risk
    st.session_state["section_scores"] = section_scores
    st.success("✅ Assessment Completed Successfully (All sections validated)")
    st.switch_page("pages/results.py")