import streamlit as st
import pandas as pd

st.title("Product Performance Dashboard")
st.subheader("2024 Quartly Sales Overview")

target_sales = st.number_input("Enter Target Sale (USD)", min_value = 500, max_value = 5000, value = 1500)

selected_quarter = st.selectbox("Select Quarter", ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"])

data = {
  "product": ["A", "B", "C"],
  "Q1 2024": [1200, 850, 950],
  "Q2 2024": [1500, 920, 880],
  "Q3 2024": [1300, 1050, 1200],
  "Q4 2024": [1600, 1100, 1400]
}

df = pd.DataFrame(data)

st.dataframe(df)

if st.button("Check Target Achievement"):
  total_sales = df[selected_quarter].sum()
  if total_sales >= target_sales:
    st.write(f"Target archieved! Total sales: ${total_sales}")
  else:
    st.write(f"Target not met. Total sales: ${total_sales:,} (need ${target_sales-total_sales:,} more)")

