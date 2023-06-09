# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16LauCre2vjIOyboXO_Pe9Vzj8ierfDVq
"""


from sklearn import preprocessing
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import seaborn as sns
import pickle 
from streamlit_option_menu import option_menu

filename ='final_model_1.sav'
loaded_model = pickle.load(open(filename, 'rb'))
df = pd.read_csv('clustered_customer_data_1.csv')
df.drop(columns = ['Unnamed: 0'], inplace = True)
df.head()

st.set_option('deprecation.showPyplotGlobalUse',False)
st.title('Customer Segmentation Prediction')

from io import StringIO

with st.sidebar:
  selected = option_menu("CHOOSE",
                         ['EXISTING',
                          'NEW DATA SET'])
if(selected == 'EXISTING'):
  st.title('Prediction')
  col1,col2,col3,col4,col5 = st.columns(5)
  with col1:
    CustomerID = st.number_input(label = 'CustomerID', step = 1)
  with col2:
    Gender = st.selectbox("choose one 1: Female, 0: Male", [1, 0])
  with col3:
    Age = st.number_input(label = 'Age', step = 1)
  with col4:
    income = st.number_input(label = 'income', step = 1)
  with col5:
    score = st.number_input(label = 'score', step = 1)

  clust_pred = ' '
  
  data = [[Gender, Age, income, score]]
  if(st.button('Predict the Cluster')):
    clust_pred = loaded_model.predict(data)[0]
    if clust_pred == 0:
      st.write('Data Belongs to ',clust_pred,'Segment')
      st.write('they EARN High & SPEND High')
      st.write('SO you can --------')
      st.balloons()
    if clust_pred == 1:
      st.write('Data Belongs to ',clust_pred,'Segment')
      st.write('they EARN Average & SPEND Average')
      st.write('SO you can --------')
      st.balloons()
    if clust_pred == 2:
      st.write('Data Belongs to ',clust_pred,'Segment')
      st.write('they EARN Low & SPEND High')
      st.write('SO you can --------')
      st.balloons()
    if clust_pred == 3:
      st.write('Data Belongs to ',clust_pred,'Segment')
      st.write('they EARN Low & SPEND Low')
      st.write('SO you can --------')
      st.balloons()
    if clust_pred == 4:
      st.write('Data Belongs to ',clust_pred,'Segment')
      st.write('they EARN High & SPEND Low')
      st.write('SO you can --------')
      st.balloons()
        
if (selected == 'NEW DATA SET'):
  st.title('Upload the .csv file')
  st.warning('the .csv file must contain columns as CustomerID, Gender, Age, score,income only')
  uploaded_file = st.file_uploader('choose file')
  if uploaded_file is not None:
    byte_data = uploaded_file.getvalue()
    st.write(byte_data)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    string_data = string.read()
    st.write(string_data)

    new_df = pd.read_csv(uploaded_file)
