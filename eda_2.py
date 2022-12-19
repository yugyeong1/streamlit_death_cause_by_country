import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from PIL import Image

def run_eda2():
# 국가별 사망원인 데이터프레임
    st.text(' ')
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

    

    st.text(' ')

    
    col1, col2, col3 = st.columns(3)

    # image 사이트 참고 https://www.printableworldflags.com/flag-icon
    with col1 :
        img = ('https://www.printableworldflags.com/icon-flags/48/'+ my_choice +'.png')
        st.image(img, use_column_width= True)
        
    with col2 :
        st.text(' ')
        st.text(' ')
        st.text(' ')
        st.markdown('######  선택한 나라의 Total 사망자 수')
        st.dataframe(death_cause[death_cause['Country Name'] == my_choice][['Country Name', 'total of death']])

    with col3 :
        st.text(' ')


    data = death_cause[death_cause['Country Name'] == my_choice].iloc[:,0:-1].set_index('Country Name')
    data_top10 = data.sum().sort_values(ascending= False).head(15)
    data_top10 = data_top10.to_frame().reset_index()
    data_top10.rename(columns= {'index' : 'diseases', 0: 'Count of Death'}, inplace= True)


    st.text(' ')
    st.text(' ')
    st.text(' ')
    st.markdown('##### 선택한 나라의 사망원인 Top 15 를 차트로 나타냅니다.')
    fig2 = px.bar(data_top10, x= 'diseases', y= 'Count of Death', title= 'Cause of death Top 15')
    st.plotly_chart(fig2)

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

