import pandas as pd
import numpy as np
import joblib
import streamlit as st

classifier = joblib.load('pipeline.pkl')

def predict_churn(Gender,Married,Dependents,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):

    prediction = classifier.predict(pd.DataFrame({'Gender':[Gender],'Married':[Married],'Dependents':[Dependents],'ApplicantIncome':[ApplicantIncome],
                                                  'CoapplicantIncome':[CoapplicantIncome],'LoanAmount':[LoanAmount],'Loan_Amount_Term':[Loan_Amount_Term],
                                                  'Credit_History':[Credit_History],'Property_Area':[Property_Area]}))


    return prediction[0]


def main():
    st.title('Loan prediction')
    html_temp="""
                <div style="background-color:red">
                <h2 style="color:white;text-align:center;">This is a Loan prediction App </h2>
                </div>
              """
    st.markdown(html_temp,unsafe_allow_html=True)

    Gender = st.radio('pick your Gender',['Male', 'Female'])
    Married = st.radio('Married?',['Yes', 'No'])
    Dependents =st.radio('Dependents?',['0', '1', '2', '3+'])
    ApplicantIncome = st.text_input('ApplicantIncome','put your ApplicantIncome')
    CoapplicantIncome = st.text_input('CoapplicantIncome','put your CoapplicantIncome')
    LoanAmount = st.text_input('LoanAmount','put your LoanAmount')
    Loan_Amount_Term = st.text_input('Loan_Amount_Term','put your Loan_Amount_Term')
    Credit_History = st.radio('Credit_History?',['0', '1'])
    Property_Area = st.radio('Property_Area',['Urban', 'Semiurban', 'Rural'])

    result =""

    if st.button('predict'):
        result = predict_churn(Gender,Married,Dependents,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
    st.success('this customer is {}'.format(result))


if __name__ =='__main__':
    main()




