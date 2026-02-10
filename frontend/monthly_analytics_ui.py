import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def monthly_analytics_tab():
    st.title("Monthly Expense Trends")

    # Allow user to select a year
    selected_year = st.number_input("Select Year", min_value=2020, max_value=2030, value=2024, step=1)

    if st.button("Show Monthly Breakdown"):
        # Call the new API endpoint
        response = requests.get(f"{API_URL}/analytics/monthly/{selected_year}")

        if response.status_code == 200:
            data = response.json()

            if data:
                # Convert list of dictionaries to DataFrame for the chart
                df = pd.DataFrame(data)

                # Format the totals for better readability
                df['formatted_total'] = df['total'].apply(lambda x: f"${x:,.2f}")

                st.subheader(f"Expenses in {selected_year}")

                # Bar Chart: X-axis = Month Name, Y-axis = Total
                st.bar_chart(data=df.set_index("month_name")['total'])

                # Display Data as a Table as well
                st.write("Detailed Breakdown:")
                st.table(df[['month_name', 'formatted_total']].rename(columns={
                    'month_name': 'Month',
                    'formatted_total': 'Total Expense'
                }))
            else:
                st.info(f"No expenses found for the year {selected_year}.")
        else:
            st.error("Failed to fetch data from server.")