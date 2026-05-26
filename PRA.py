import streamlit as st # type: ignore

st.title("Performance Risk Assessment Scoring Tool")

# Score map
score_map = {
    "Yes": 5, "Maybe": 3, "No": 1, "N/A": 0,
    "80+": 5, "60-80%": 4, "40-60%": 3, "20-40%": 2, "<20%": 1,
    ">50%": 5, "25-49%": 4, "10-24%": 3, "5-9%": 2, "<5%": 1,
    ">10": 5, "7-9": 4, "5-6": 3, "1-4": 2,
    "10,000+": 5, "5000-9999": 4, "1000-4999": 3, "100-999": 2, "<100": 1,
    "100+": 5, "50-99": 4, "10-49": 3, "5-9": 2, "<5": 1,
    "Both": 5, "In House": 4, "Vendor": 3, "No(COTS)": 1
}

questions = [
    ("Is the Business Service Critical?", ["Yes","No","Maybe","N/A"]),
    ("What is the current capacity utilisation of the Service?", ["80+","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("Volume - number of concurrent users?", ["10,000+","5000-9999","1000-4999","100-999","<100","N/A"]),
    ("Volume - anticipated transaction rate(TPS- transactions per second)?", ["100+","50-99","10-49","5-9","<5"]),
    ("Is the Service currently supported by both in-house and vendor teams?", ["Both","In House","Vendor","No(COTS)"]),
    ("Are the Service's dependencies (e.g., databases, external APIs) also critical?", ["Yes","No","Maybe","N/A"]),
    ("How frequently does the Service experience performance issues?", [">10","7-9","5-6","1-4","N/A"]),
    ("What percentage of the Service's users are affected by performance issues?", [">50%","25-49%","10-24%","5-9%","<5%","N/A"]),
    ("What percentage of the Service's transactions are affected by performance issues?", [">50%","25-49%","10-24%","5-9%","<5%","N/A"]),
    ("How long do performance issues typically last?", [">1 hour","30 min-1 hour","10-30 min","<10 min","N/A"]),
    ("How quickly can the Service be restored to normal performance after an issue?", [">1 hour","30 min-1 hour","10-30 min","<10 min","N/A"]),
    ("How well-documented are the Service's performance issues and resolutions?", ["Well-documented","Somewhat documented","Poorly documented","N/A"]),
    ("How often are performance issues reviewed and addressed in the Service's maintenance cycle?", ["Regularly","Occasionally","Rarely","N/A"]),
    ("How much of the Service's codebase is custom-built vs. using COTS (Commercial Off-The-Shelf) components?", ["100% Custom","75% Custom","50% Custom","25% Custom","0% Custom(COTS)","N/A"]),
    ("How many critical performance issues has the Service experienced in the past year?", ["10+","7-9","5-6","1-4","0","N/A"]),
    ("How many users have been impacted by critical performance issues in the past year?", ["10,000+","5000-9999","1000-4999","100-999","<100","N/A"]),
    ("How many transactions have been impacted by critical performance issues in the past year?", ["100,000+","50,000-99,999","10,000-49,999","1,000-9,999","<1,000","N/A"]),
    ("How quickly are performance issues typically detected?", [">1 hour","30 min-1 hour","10-30 min","<10 min","N/A"]),
    ("How quickly are performance issues typically resolved?", [">1 hour","30 min-1 hour","10-30 min","<10 min","N/A"]),
    ("How well does the Service's architecture support performance under load?", ["Excellent","Good","Fair","Poor","N/A"]),
    ("How much redundancy is built into the Service to mitigate performance issues?", [">50%","25-49%","10-24%","5-9%","<5%","N/A"]),
    ("How often are performance tests conducted on the Service?", ["Regularly","Occasionally","Rarely","N/A"]),
    ("How comprehensive are the Service's performance monitoring and alerting systems?", ["Comprehensive","Adequate","Limited","None","N/A"]),
    ("How well does the Service's team understand and manage performance risks?", ["Excellent","Good","Fair","Poor","N/A"] ),
    ("How much of the Service's performance risk is mitigated by existing controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is residual (i.e., not mitigated by controls)?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is accepted (i.e., knowingly not mitigated)?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is transferred (e.g., through insurance or outsourcing)?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is avoided (e.g., by not implementing certain features)?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is shared (e.g., through partnerships or collaborations)?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is accepted by stakeholders?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is communicated to stakeholders?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is monitored and reviewed over time?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is documented and tracked?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by technical controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by organizational controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by process controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by people controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by external controls (e.g., third-party services)?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by internal controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by preventive controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by detective controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by corrective controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
    ("How much of the Service's performance risk is mitigated by compensating controls?", [">80%","60-80%","40-60%","20-40%","<20%","N/A"]),
]
responses = []

for q, opts in questions:
    ans = st.radio(q, opts)
    responses.append(ans)

if st.button("Calculate Score"):
    total = sum(score_map.get(r, 0) for r in responses)

    if total >= 50:
        risk = "HIGH RISK"
    elif total >= 30:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    st.metric("Total Score", total)
    st.metric("Risk Level", risk)

    st.bar_chart(section_scores) # type: ignore
    st.subheader(f"Total Score: {total}")
    st.subheader(f"Risk Level: {risk}")