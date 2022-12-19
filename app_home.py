import streamlit as st
import pandas as pd
from PIL import Image
from tkinter.tix import COLUMN
from pyparsing import empty



def run_home_app() : 
    # 국가별 사망원인 데이터프레임
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)
    st.text(' ')


    st.markdown('##### 국가별 사망 원인 데이터를 이용하여 분석한 앱입니다.')
    st.text('이 앱은 국가별 사망 원인 데이터프레임을 이용하여서, 전세계에서 어떤 국가에 가장 많은 사망자가 있는지, 어떤 질병때문에 가장 많이 사망 하였는지에 대해서 분석한 앱입니다. ')
    st.text(' ')

    col1, col2 = st.columns(2)


    with col1:
        img = Image.open('data/국기.png')
        # 웹브라우저 가로 사이즈와 일치하게 출력
        st.image(img)

    with col2:
         # 정렬하여서 데이터프레임 보여주기 - 나라이름으로, 사망자가 많은 순으로 
        st.text('')
        status = st.radio(' ', ['나라이름으로 정렬하기', '총 사망자 수가 많은 순으로 정렬'] )

    st.text(' ')
    st.text(' ')

    if status == '나라이름으로 정렬하기' :
        st.dataframe(death_cause.sort_values('Country Name', ascending= True))

    elif status == '총 사망자 수가 많은 순으로 정렬':
        st.dataframe(death_cause.sort_values('total of death', ascending= False))

