import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category_ui  import analytics_tab
from monthly_analytics_ui import monthly_analytics_tab

API_URL ="http://127.0.0.1:8000"

st.title("Expense Management App")

tab_1, tab_2, tab_3 = st.tabs(["Add/Update","Analytics by Category", "Monthly Analysis"])

with tab_1:
    add_update_tab()
with tab_2:
    analytics_tab()
with tab_3:
    monthly_analytics_tab()



