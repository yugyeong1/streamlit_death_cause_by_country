# streamlit 라이브러리를 사용하기 위한 임포트문 작성
import streamlit as st
from app_home import run_home_app
from app_EDA import run_eda_app
from app_about import run_about_app
from PIL import Image


def main() :
    st.markdown('## 국가별 사망 원인 분석')


    menu = ['Home', 'EDA', 'About']
 
    choice = st.sidebar.selectbox('메뉴', menu)

    img2 = st.sidebar.image('https://w7.pngwing.com/pngs/269/15/png-transparent-world-map-globe-world-map-border-miscellaneous-blue.png')


    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'About' :
        run_about_app()


if __name__ == '__main__' :
    main()