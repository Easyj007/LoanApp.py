# -*- coding: utf-8 -*-
import pandas as pd
#import numpy as np
import streamlit as st 
import joblib


#load saved model
model = joblib.load('loan_predictor.pkl')
#add streamlit title
st.title("LOAN FLAG APP")

#User Input
#latitude_gps_log	longitude_gps_log	term_days_log	loan_number_log
loan_number=st.slider('Number of loans',1,30,1, step=1)
loan_amount = st.slider('loan_amount(#)',10000,60000,10000,step=5000)
total_due = st.number_input('total_due(#)',10000,150000,10000,step=5000)
term_days = st.selectbox('term_days',[15,30,45,60,75,90])
birth_date =st.date_input('Birth date', value=pd.to_datetime('1990-01-01'))
bank_account_type = st.selectbox('bank_account_type',['Savings','Current','Other'])
longitude_gps= st.slider('longitude_gps', -180.1,180.0,3.1, step=0.1) 
latitude_gps = st.slider('latitude_gps', -90.0,90.0,3.5, step=0.1)
bank_name_clients = st.selectbox('bank_name_clients', ['GT Bank','Diamond Bank','EcoBank','First Bank','FCMB','Skye Bank','Access Bank','UBA','Zenith Bank'])
employment_status_clients = st.selectbox('employment_status_clients',['Permanent','Unemployed','Self-employed','Student','Retired','Contract'])
approved_date =st.date_input('approved date', value=pd.to_datetime('2017-01-01'))
creation_date =st.date_input('creation date', value=pd.to_datetime('2017-01-01'))
system_loan_id =st.number_input('system_loan_id', 301910000,302000000,301958834, step=100)
#'latitude_gps_log'
    #'longitude_gps_log'
    #'term_days_log'
    #'loan_number_log'

#Predict button
if st.button("Predict the loan flag"):
    data ={
        "loan_number":[loan_number],
        "loan_amount":[loan_amount],
        "total_due":[total_due],
        "term_days": [term_days],
        "birth_date": [birth_date],
        "bank_account_type": [bank_account_type],
        "longitude_gps": [longitude_gps],
        "latitude_gps": [latitude_gps],
        "bank_name_clients": [bank_name_clients],
        "employment_status_clients": [employment_status_clients],
        "approved_date": [approved_date],
        "creation_date": [creation_date],
        "system_loan_id": [system_loan_id]
        }
    #convert into a dataframe
    df =pd.DataFrame(data)
    
    flag = model.predict(df)
    prediction= flag[0]
    
    st.success(f"client loan flag is: {prediction} flag")