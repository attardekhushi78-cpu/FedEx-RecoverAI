import streamlit as st
import pandas as pd

st.set_page_config(page_title="FedEx RecoverAI", layout="wide")

st.title("📦 FedEx DCA Management Portal")
st.sidebar.header("Agency Access")

# Mock data to show "Centralized Case Tracking"
data = {
    'Customer ID': ['C101', 'C102', 'C103'],
    'Debt Amount': [5000, 12000, 300],
    'Days Overdue': [15, 60, 5],
    'Assigned Agency': ['Agency A', 'Agency B', 'Internal'],
    'Status': ['In Progress', 'Escalated', 'Pending']
}
df = pd.DataFrame(data)

st.subheader("Active Case Overview")
st.dataframe(df, use_container_width=True)

# Visualize "Limited Performance Visibility" solution
st.subheader("Recovery Analytics")
st.bar_chart(df.set_index('Assigned Agency')['Debt Amount'])
