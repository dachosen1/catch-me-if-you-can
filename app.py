import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import streamlit as st
from model import score_model

st.title("Accenture Hackathon")
st.markdown("**Team**: Cath me if you can")
st.markdown("**Problem Statement**: Anomally detection for financial services")
st.markdown("The financial services sector is one of the first in line to pick up the benefits of AI and Machine "
            "Learning. Digital banking opened the sector to new fraud scenarios, which are posing a great challenge "
            "for human analysts, due to their complexity, speed and scale. In this scenario you will use a dataset "
            "created specifically for fraud detection in financial services.")

unit_of_time = st.sidebar.number_input('Unit of time in the real world', 1, 1000, 100)
transaction_amount = st.sidebar.number_input('Amount of the Transaction', 1, 100000000000, 1000)

with st.form("my_form"):
    st.write("Data Exploration Results")
    checkbox_val = st.checkbox("See results ")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:

        st.write("sample chart")
        chart_data = pd.DataFrame(
            np.random.randn(50, 3),
            columns=["a", "b", "c"])
        st.bar_chart(chart_data)

        # Add histogram data
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        # Group data together
        hist_data = [x1, x2, x3]

        group_labels = ['Group 1', 'Group 2', 'Group 3']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)

        df = pd.DataFrame(
            np.random.randn(200, 3),
            columns=['a', 'b', 'c'])

        c = alt.Chart(df).mark_circle().encode(
            x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

        st.altair_chart(c, use_container_width=True)

st.sidebar.selectbox(label="Payment Type", options=["Cash-In", "Cash-Out", "Debit", "Payment", "Transfer"])
old_balance = st.sidebar.number_input("Initial balance before the transaction", 1, 100000000000, 1000)
new_balance = st.sidebar.number_input("customer's balance after the transaction", 1, 100000000000, 1000)

if st.sidebar.button('Run'):
    st.info("""The Machine Learning Algorithm predicts the following based on the selected input 
            """)

    score = score_model(data=data)
    st.write("Predicted Fraud", score[0])
