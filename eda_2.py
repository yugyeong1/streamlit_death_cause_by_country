import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

def run_eda2():
# 국가별 사망원인 데이터프레임
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)

    # 유저한테서 country명을 입력 받은 후 , 입력 받은 국가의 데이터분석 결과 나타내기
    st.markdown('#### 원하는 국가의 데이터분석 결과를 보여줍니다.')
    col1, col2 = st.columns(2)

    with col1:
       input_country = st.text_input('분석 결과를 알고싶은 나라를 입력하세요.')

    with col2:
        country = death_cause[death_cause['Country Name'].str.contains(input_country, case= False)]['Country Name']
        my_choice = st.selectbox(' ', country.values)

    # 선택한 나라의 데이터프레임 / 컬럼 선택시 그 컬럼 데이터만 나타내기
    selected_list = st.multiselect('원하는 컬럼을 선택하세요! 선택한 컬럼들의 데이터를 보여줍니다.', death_cause[death_cause['Country Name'] == my_choice].columns)
   
    if selected_list :
        st.dataframe(death_cause[death_cause['Country Name'] == my_choice][selected_list]) 
    else :
        st.dataframe(death_cause[death_cause['Country Name'] == my_choice])



