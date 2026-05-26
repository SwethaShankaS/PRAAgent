import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Performance Assessment Results", layout="wide")
st.title("📊 Performance Assessment Results")

# -------------------------
# LOAD DATA
# -------------------------
if "section_scores" not in st.session_state:
    st.warning("Complete assessment first")
    st.stop()

total_score = st.session_state["total_score"]
risk = st.session_state["risk"]
section_scores = st.session_state["section_scores"]

# -------------------------
# METRICS
# -------------------------
col1, col2 = st.columns(2)
col1.metric("Total Score", total_score)
col2.metric("Risk Level", risk)

# -------------------------
# PIE CHART
# -------------------------
fig = px.pie(
    names=list(section_scores.keys()),
    values=list(section_scores.values()),
    title="Section Contribution"
)

fig.update_traces(textinfo="label+percent")
st.plotly_chart(fig, use_container_width=True)

# -------------------------
# TESTING STRATEGY
# -------------------------
st.subheader("🧪 Recommended Testing Strategy")

if "HIGH" in risk:
    st.error("""
🔴 HIGH RISK:
• Full Performance Testing
• Load + Stress Testing
• End-to-End Integration Testing
• Failover Testing
• Security Testing
""")

elif "MEDIUM" in risk:
    st.warning("""
🟠 MEDIUM RISK:
• Targeted Performance Testing
• Regression Testing
• Integration Testing
""")

else:
    st.success("""
🟢 LOW RISK:
• Functional Testing
• Smoke Testing
• Monitoring
""")

# -------------------------
# SECTION EXPLANATION
# -------------------------
st.subheader("📘 Interpretation")

st.write("Higher section score = higher risk or complexity in that area.") 
st.write("If 'Code Quality' is high, focus on code reviews and refactoring to improve performance.")
st.write("If 'Testing Coverage' is low, prioritize adding performance tests to cover critical paths and scenarios.")
st.write("If 'Release Timeline' is tight, focus on critical performance tests and monitoring to catch any last-minute issues before deployment.")
st.write("If 'Team Experience' is low, consider bringing in external expertise or investing in training to build internal capabilities.")
st.write("If 'Code Quality' is high, prioritize code reviews and regression testing.")
st.write("If 'Resource Utilisation' is high, focus on load testing and monitoring to ensure the infrastructure can handle expected loads.")
st.write("If 'Infrastructure' is high, focus on load testing and failover strategies.")
st.write("If 'Team Experience' is high, consider additional training and knowledge sharing sessions.\nIf the Today’s date is close to the release date, prioritize testing and monitoring to catch last-minute issues.")
st.write("If the codebase is large and complex, focus on code quality improvements and targeted performance testing to address potential bottlenecks.")
st.write("If the infrastructure is complex or has many dependencies, focus on integration and end-to-end testing to ensure all components work together under load.")
st.write("If the codebase has a history of performance issues, prioritize code quality improvements and targeted performance testing to address known bottlenecks.")
st.write("If the release date is approaching, focus on critical performance tests and monitoring to catch any last-minute issues before deployment.")
st.write("If the total Score is above 400, it indicates a high risk of performance issues, and a comprehensive testing strategy should be implemented to mitigate potential problems before release.")
st.write("If the score is between 200 and 400, it indicates a moderate risk, and targeted testing should be prioritized to address specific areas of concern.")
st.write("If the score is below 200, it indicates a low risk, and standard testing practices should be sufficient to ensure performance quality.")

