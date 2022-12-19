import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from eda_1 import run_eda1
from eda_2 import run_eda2

def run_eda_app() :
    menu = ['전체 사망자 수, 사망원인 분석', '선택한 국가의 데이터분석']
 
    choice_eda = st.sidebar.selectbox('메뉴', menu)

    if choice_eda == '전체 사망자 수, 사망원인 분석' :
        run_eda1()

    elif choice_eda == '선택한 국가의 데이터분석' :
        run_eda2()


