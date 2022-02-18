import pandas as pd
import streamlit as st

from model import score_model

st.title("Accenture Hackathon")
st.markdown("**Team**: Catch me if you can")
st.markdown("**Problem Statement**: Anomaly detection for financial services")
st.markdown("The financial services sector is one of the first in line to pick up the benefits of AI and Machine "
            "Learning. Digital banking opened the sector to new fraud scenarios, which are posing a great challenge "
            "for human analysts, due to their complexity, speed and scale. In this scenario you will use a dataset "
            "created specifically for fraud detection in financial services.")


transaction_amount = st.sidebar.number_input('amount', 0, 100000000000, 1000)
payment_type = st.sidebar.selectbox(label="Type", options=["TRANSFER", "CASH-IN", "CASH-OUT", "DEBIT", "PAYMENT"])


old_balance_org = st.sidebar.number_input("oldbalanceOrg", 0, 100000000000, 105867)
new_balance_org = st.sidebar.number_input("newbalanceOrig", 0, 100000000000, 90540)


old_balance_dest = st.sidebar.number_input("oldbalanceDest", 0, 100000000000, 0)
new_balance_dest = st.sidebar.number_input("newbalanceDest", 0, 100000000000, 0)

flagged_fraud = st.sidebar.selectbox(label="Flags illegal attempts to transfer more than 200.000 in a single "
                                           "transaction",
                                     options=["true", "false"])

flagged_dict = {
    "true": 1,
    "false": 0
}

data = pd.DataFrame([{
    "type": payment_type,
    "step": 250,
    "amount": transaction_amount,
    "nameOrig": "C353296011",
    "oldbalanceOrg": old_balance_org,
    "newbalanceOrig": new_balance_org,
    "nameDest": "C1182908789",
    "oldbalanceDest": old_balance_dest,
    "newbalanceDest": new_balance_dest,
    "isFlaggedFraud": flagged_dict[flagged_fraud]
}])

if st.sidebar.button('Run'):

    st.info(""" 
    The application uses a light GPM model to classify transactions as Fraud!  
            """)

    st.info("""Is the Transaction Fraud? 
            """)

    score = score_model(data=data)
    st.header(score[0])
