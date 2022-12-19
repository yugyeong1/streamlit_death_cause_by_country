import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


def run_eda_app() :
    # 국가별 사망원인 데이터프레임
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)

    st.line_chart(data=death_cause[['Country Name', 'total of death']], x='Country Name', y= 'total of death', width=0, height=0)
    

