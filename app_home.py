import streamlit as st
import pandas as pd
from PIL import Image
#from tkinter.tix import COLUMN
#from pyparsing import empty

def run_home_app() : 
    # 국가별 사망원인 데이터프레임
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)
    st.text(' ')


    st.markdown('##### 국가별 사망 원인 데이터를 이용하여 분석한 앱입니다.')

    with st.expander('대시보드 앱 설명 : ') :
        st.text('이 앱은 2020년도 국가별 사망 원인 데이터프레임을 이용하여서,')
        st.text('전세계에서 어떤 국가에 가장 많은 사망자가 있는지, ')
        st.text('어떤 질병때문에 가장 많이 사망 하였는지에 대해서 분석한 앱입니다. ')
        st.text('그리고 사용자가 선택한 나라에 대해서 분석한 결과를 나타냅니다.')
    st.text(' ')

    col1, col2 = st.columns(2)


    with col1:
        img = Image.open('data/국기.png')
        # 웹브라우저 가로 사이즈와 일치하게 출력
        st.image(img)

    with col2:
         # 정렬하여서 데이터프레임 보여주기 - 나라이름으로, 사망자가 많은 순으로 
        st.text('')
        status = st.radio(' ', ['나라 이름으로 정렬하기', '총 사망자 수가 많은 순으로 정렬'] )

    st.text(' ')
    st.text(' ')

    if status == '나라 이름으로 정렬하기' :
        st.dataframe(death_cause.sort_values('Country Name', ascending= True))

    elif status == '총 사망자 수가 많은 순으로 정렬':
        st.dataframe(death_cause.sort_values('total of death', ascending= False))

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

