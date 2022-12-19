import streamlit as st
import pandas as pd
import numpy as np

def run_about_app() : 
    st.text(' ')
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)

    st.markdown('#### 데이터분석에 사용한 데이터프레임')
    st.text(' ')
    st.dataframe(death_cause)
    st.info('데이터출처 https://www.kaggle.com/datasets/majyhain/death-cause-by-country')

