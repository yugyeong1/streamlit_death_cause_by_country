<br/>
<div align="center">

#   📌 국가별 사망 원인 데이터를 이용하여 웹 대시보드 앱 개발

</div>  
<br/>
<div align="cecnter">

### 🌟 Platfroms & languages 🌟

</div>

<div>
  <img src="https://img.shields.io/badge/Python-007396?style=flat&logo=Python&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter Notebook-E34F26?style=flat&logo=Jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat&logo=Amazon AWS&logoColor=white" />
  <img src="https://img.shields.io/badge/EC2-FF9900?style=flat&logo=Amazon EC2&logoColor=white" />
</div>  

<br/>

<div align="left">

### 🛠 Tools 🛠

</div>  

<div>
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white"/> 
<img src="https://img.shields.io/badge/Github-000000?style=flat&logo=Github&logoColor=white"/>
</div>

<br/> 






#### 📌 사용한 라이브러리

<div>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white"/> 
<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/matplotlib-EBAF00?style=flat&logo=matplotlib&logoColor=white"/>
<img src="https://img.shields.io/badge/seaborn-52BBE6?style=flat&logo=seaborn&logoColor=white"/>
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=Plotly&logoColor=white"/> 
<img src="https://img.shields.io/badge/PIL-14A0C4?style=flat&logo=PIL&logoColor=white"/>
</div>

<br/>

### 📌 데이터분석  

이 앱은 2020년도 국가별 사망 원인 데이터프레임을 이용하여서,  
전세계에서 어떤 국가에 가장 많은 사망자가 있는지,  
어떤 질병때문에 가장 많이 사망 하였는지에 대해서 분석한 앱입니다.  
그리고 사용자가 선택한 나라에 대해서 분석한 결과를 나타냅니다.  


데이터를 분석하여서, 국가별 사망자 총 합 데이터를 plotly 의 line chart 로 나타내었고,  
전 국가가 어떤 질병으로 인해 많이 사망했는지에 대한 데이터를 plotly 의 bar 차트를 이용하여서 나타냈습니다.  

그리고 사용자가 선택한 국가에 대해서도 분석한 결과를 나타낼 수 있도록 하였습니다.  
사용자가 국가명을 입력하면 contains 함수를 이용하여, 검색 결과가 포함된 나라를 selectbox 를 이용하여 선택할 수 있도록 하였고,  
선택한 나라의 데이터프레임을 나타나게 하였습니다.  
선택한 나라의 사망자 총 합수와, 어떤 질병으로 사망했는지에 대한 데이터를 plotly 의 bar 차트를 이용하여서 나타냈습니다.  



<br/>


### 📌 AWS EC2 배포, Github Actions 이용

AWS 의 EC2 서버를 이용하여서, 앱 대시보드를 서버에 배포 하였고,
  
Github Actions 기능을 이용하여서, 코드 수정사항을 Github 에 push 할 때마다  
putty 에 접속하지 않아도, 자동으로 배포할 수 있도록 하였습니다.  

<br/>

<div align="left">

### 📌 Link


http://ec2-3-36-60-118.ap-northeast-2.compute.amazonaws.com:8502/


</div>  

<br/>
<br/>

### 데이터분석에 이용한 csv 데이터 컬럼

#### Death Cause by Country
<br/>

Country Name : 국가명  
Covid-19 Deaths : Covid-19 질병으로 의한 사망자 수  
Cardiovascular disease : 심혈관 질병으로 인한 사망자 수  
Respiratory disease : 호흡기 질병으로 인한 사망자 수  
kidney disease : 신장 질병으로 인한 사망자 수  
Neonatal disorders : 신생아 장애로 인한 사망자 수  
meningitis : 수막염으로 인한 사망자 수  
Malaria : 말라리아로 인한 사망자 수  
Interpersonal violence : 대인 폭력으로 인한 사망자 수  
HIV/AIDS : 인간 면역 결핍 바이러스로 인한 사망자 수  
Tuberculosis : 결핵으로 인한 사망자 수  
Maternal disorders : 모성 장애로 인한 사망자 수  
lower respiroraty issues : 낮은 호흡 문제 인한 사망자 수  
Alcohol : 알콜로 인한 사망자 수  
diarrheal disorder : 설사 장애로 인한 사망자 수  
poisoning : 중독으로 인한 사망자 수  
nutritional deficiency : 영양결핍으로 인한 사망자 수  
alzhimer : 알츠하이머 치매로 인한 사망자 수  
parkinson diseases : 파키슨병으로 인한 사망자 수  
acute hepatitis : 급성 간염으로 인한 사망자 수  
digestive diseases : 소화기 질환으로 인한 사망자 수  
cirrhosis : 경화증으로 인한 사망자 수  
protein energy deficiency : 단백질 에너지 결핍으로 인한 사망자 수  
neoplasms : 신생물에 의한 사망자 수  
fire heat : 화재로 인한 사망자 수  
drowning : 익사로 인한 사망자 수  
drug disorders : 약물 장애로 인한 사망자 수  
road injuries : 교통사고로 인한 사망자 수  
enviromental issues : 환경문제로 인한 사망자 수  
self harm : 자해로 인한 사망자 수  
conflict and terrorism : 갈등과 테러로 인한 사망자 수  
diabetes : 당뇨병으로 인한 사망자 수  
total of death : 각 나라별 총 사망자 수  


### 데이터출처 https://www.kaggle.com/datasets/majyhain/death-cause-by-country
