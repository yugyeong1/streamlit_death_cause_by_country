import streamlit as st
import pandas as pd
import numpy as np

def run_about_app() : 
    st.text(' ')
    death_cause = pd.read_csv('data/Death Cause Reason by Country.csv')
    death_cause.drop(columns= 'Unnamed: 32', axis= 1, inplace= True)
    death_cause['total of death'] = death_cause.sum(axis=1, numeric_only=True)

    