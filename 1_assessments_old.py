import streamlit as st # type: ignore

st.title("Performance Risk Assessment")

# -------------------------
# SESSION STATE
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

# -------------------------
# SCORE MAP
# -------------------------
score_map = {
    "Yes": 5, "Maybe": 3, "No": 1, "N/A": 0,
    "80+": 5, "60-80%": 4, "40-60%": 3, "20-40%": 2, "<20%": 1,
    ">50%": 5, "25-49%": 4, "10-24%": 3, "5-9%": 2, "<5%": 1,
    ">10": 5, "7-9": 4, "5-6": 3, "1-4": 2,
    "10,000+": 5, "5000-9999": 4, "1000-4999": 3, "100-999": 2, "<100": 1,
    "100+": 5, "50-99": 4, "10-49": 3, "5-9": 2, "<5": 1,
    "Both": 5, "External": 4, "Internal": 3, "Vendor": 3, "In House": 4, "No(COTS)": 1
}

# -------------------------
# STEPS (ALL QUESTIONS)
# -------------------------
steps = [

# 1
{
"title": "Service Identification",
"questions": [
("Users of this Service?", ["Internal","External","Both","N/A"]),
("Is the Business Service Critical?", ["Yes","No","Maybe","N/A"]),
("Does this service impact critical Services/Products?", ["Yes","No","Maybe","N/A"]),
("Is the Service custom coded?", ["Both","Vendor","In House","No(COTS)","N/A"])
]
},

# 2
{
"title": "Capacity & Growth",
"questions": [
("Current capacity utilisation?", ["80+","60-80%","40-60%","20-40%","<20%","N/A"]),
("Current annual growth rate?", [">50%","25-49%","10-24%","5-9%","<5%","N/A"]),
("Volumetric growth change?", [">50%","25-49%","10-24%","5-9%","<5%","N/A"]),
("Concurrent users?", ["10,000+","5000-9999","1000-4999","100-999","<100","N/A"]),
("Transactions per second?", ["100+","50-99","10-49","5-9","<5","N/A"])
]
},

# 3
{
"title": "Performance & Stability",
"questions": [
("Breakpoint known?", ["Yes","No","Maybe","N/A"]),
("Performance/stability issues in last 6 months?", ["Yes","No","Maybe","N/A"]),
("PNV performed in last 18 months?", ["Yes","No","Maybe","N/A"]),
("Meets NFR requirements?", ["Yes","No","Maybe","N/A"]),
("High I/O or batch loads expected?", ["Yes","No","Maybe","N/A"])
]
},

# 4
{
"title": "Architecture & Dependencies",
"questions": [
("Number of interfacing systems?", [">10","7-9","5-6","1-4","N/A"]),
("Number of 3rd party components?", [">10","7-9","5-6","1-4","N/A"]),
("Shares infrastructure with other services?", ["Yes","No","Maybe","N/A"]),
("Impacts other systems?", ["Yes","No","Maybe","N/A"])
]
},

# 5
{
"title": "Change & Deployment",
"questions": [
("Does change introduce new functionality?", ["Yes","No","Maybe","N/A"]),
("Any code/config changes?", ["Yes","No","Maybe","N/A"]),
("Infra/OS/DB changes?", ["Yes","No","Maybe","N/A"]),
("Is this a new or migrating platform?", ["Yes","No","Maybe","N/A"])
]
},

# 6
{
"title": "Risk & Sensitivity",
"questions": [
("Customer/financially sensitive functions?", ["Yes","No","Maybe","N/A"])
]
}

]

# -------------------------
# PROGRESS BAR
# -------------------------
progress = (st.session_state.step) / len(steps)
st.progress(progress)

st.write(f"Step {min(st.session_state.step + 1, len(steps))} of {len(steps)}")

# -------------------------
# NAVIGATION
# -------------------------
def next_step():
    current = steps[st.session_state.step]

    # ✅ VALIDATION
    for i, (q, _) in enumerate(current["questions"]):
        key = f"{st.session_state.step}_{i}"
        if key not in st.session_state.responses:
            st.error(f"Please answer: {q}")
            return

    st.session_state.step += 1


def prev_step():
    st.session_state.step -= 1


# -------------------------
# STEP DISPLAY
# -------------------------
if st.session_state.step < len(steps):

    current = steps[st.session_state.step]
    st.header(current["title"])

    for i, (q, opts) in enumerate(current["questions"]):

        key = f"{st.session_state.step}_{i}"

        default = st.session_state.responses.get(key)
        index = opts.index(default) if default in opts else 0

        ans = st.radio(q, opts, index=index, key=key)
        st.session_state.responses[key] = ans

    col1, col2 = st.columns(2)

    if st.session_state.step > 0:
        col1.button("⬅ Previous", on_click=prev_step)

    if st.session_state.step < len(steps) - 1:
        col2.button("Next ➡", on_click=next_step)
    else:
        col2.button("Submit ✅", on_click=next_step)

# -------------------------
# SAVE + NAVIGATE
# -------------------------
else:

    total_score = 0
    section_scores = {}

    for step_index, step_data in enumerate(steps):

        section_score = 0

        for i, (q, _) in enumerate(step_data["questions"]):
            key = f"{step_index}_{i}"
            answer = st.session_state.responses.get(key)

            score = score_map.get(answer, 0)
            total_score += score
            section_score += score

        section_scores[step_data["title"]] = section_score

    if total_score >= 80:
        risk = "HIGH RISK"
    elif total_score >= 50:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    # Save results
    # Save results
    st.session_state["total_score"] = total_score
    st.session_state["risk"] = risk
    st.session_state["section_scores"] = section_scores

    st.success("Assessment Completed ✅")

    st.switch_page("pages/2_Results.py")