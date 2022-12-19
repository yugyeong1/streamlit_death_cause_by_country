import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


def run_eda1():
    # 국가별 사망원인 데이터프레임
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)
    

    # 국가별로 사망자수 나타내기
    st.text('')
    st.text('')
    st.markdown('##### Total number of deaths by country ')
    st.text('아래 차트는 국가별로 사망자 수의 Total 값을 나타냅니다.')
    st.line_chart(data=death_cause[['Country Name', 'total of death']], x='Country Name', y= 'total of death', width=0, height=0)


    st.text('')
    st.text(' ')
    # 어떤 질병때문에 가장 많이 사망 하였는지 나타내는 차트
    st.markdown('##### Which diseases are the most common')
    st.text('아래 차트는 어떤 질병으로 인해 사망했는지에 대해서 나타내는 차트입니다.')
    how_many = death_cause.iloc[:,1:-1].sum().sort_values().to_frame().reset_index()
    how_many.rename(columns= {'index' : 'diseases', 0: 'Count of Death'}, inplace= True)
    fig1 = px.bar(how_many, x= 'Count of Death', y= 'diseases')
    st.plotly_chart(fig1)