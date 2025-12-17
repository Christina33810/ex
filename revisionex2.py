import streamlit as st
import time

col1, col2 = st.columns(2)
with col1 :
  with expander(" Market Trends 2024"):
    st.write("Eco-friendly products: Increasing demand",
             "Online shopping: Continued growth",
             "Subscription services: Rising popularity"
            )
  growth_rate = st.slider ("Adjust growth projection(%)", min_value = 0, max_value = 30, value = 10)

with col2 :
    tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insight", "Forcast"])
    with tab1:
      sales_data = {
        "Month": ["Jan", "Feb", "Mar"],
        "Sales": [45000, 48000, 52000],
        "Customers": [320,350, 380]
      }

      df = pd.DataFrame(sales_data)
      st.table(df)

    with tab2:
      feedbacks = [            
            "Great service and fast delivery.",
            "Product quality exceeded expectations.",
            "Customer support was very helpful."
        ]

       for i, feedback in enumerate(feedbacks, start=1):
         st.write(f"{i}. {feedback}")
               
    with tab3:
      mar_sales = df[df["Month" == "Mar"]["Sales"]]
      forcasted_sales = mar_sales * (1 + growth_rate/100)

      placeholder = st.empty()

      for x in range(1,6):
        placeholder.write(f" Loading forecast ... {x*20}% complete")

      st.markdown("### The forcasted sales is ${forcasted_sale}")
  
