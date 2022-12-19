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

    with st.expander('columns 설명 : ') :
            st.text('Country Name : 국가명')
            st.text('Covid-19 Deaths : Covid-19 질병으로 의한 사망자 수')
            st.text('Cardiovascular disease : 심혈관 질병으로 인한 사망자 수')
            st.text('Respiratory disease : 호흡기 질병으로 인한 사망자 수')
            st.text('kidney disease : 신장 질병으로 인한 사망자 수')
            st.text('Neonatal disorders : 신생아 장애로 인한 사망자 수')
            st.text('meningitis : 수막염으로 인한 사망자 수')
            st.text('Malaria : 말라리아로 인한 사망자 수')
            st.text('Interpersonal violence : 대인 폭력으로 인한 사망자 수')
            st.text('HIV/AIDS : 인간 면역 결핍 바이러스로 인한 사망자 수')
            st.text('Tuberculosis : 결핵으로 인한 사망자 수')
            st.text('Maternal disorders : 모성 장애로 인한 사망자 수')
            st.text('lower respiroraty issues : 낮은 호흡 문제 인한 사망자 수')
            st.text('Alcohol : 알콜로 인한 사망자 수')
            st.text('diarrheal disorder : 설사 장애로 인한 사망자 수')
            st.text('poisoning : 중독으로 인한 사망자 수')
            st.text('nutritional deficiency : 영양결핍으로 인한 사망자 수')
            st.text('alzhimer : 알츠하이머 치매로 인한 사망자 수')
            st.text('parkinson diseases : 파키슨병으로 인한 사망자 수')
            st.text('acute hepatitis : 급성 간염으로 인한 사망자 수')
            st.text('digestive diseases : 소화기 질환으로 인한 사망자 수')
            st.text('cirrhosis : 경화증으로 인한 사망자 수')
            st.text('protein energy deficiency : 단백질 에너지 결핍으로 인한 사망자 수')
            st.text('neoplasms : 신생물에 의한 사망자 수')
            st.text('fire heat : 화재로 인한 사망자 수')
            st.text('drowning : 익사로 인한 사망자 수')
            st.text('drug disorders : 약물 장애로 인한 사망자 수')
            st.text('road injuries : 교통사고로 인한 사망자 수')
            st.text('enviromental issues : 환경문제로 인한 사망자 수')
            st.text('self harm : 자해로 인한 사망자 수')
            st.text('conflict and terrorism : 갈등과 테러로 인한 사망자 수')
            st.text('diabetes : 당뇨병으로 인한 사망자 수')
            st.text('total of death : 각 나라별 총 사망자 수')

