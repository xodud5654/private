import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import scatter_matrix

st.set_option('deprecation.showPyplotGlobalUse', False)

st.header("상황별 코드")

data= pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/heart.csv")
if st.button("data 확인"):
    st.subheader("data 확인")
    #st.write(data.isnull().values.any())
    st.write(data.isna().sum())
st.markdown("* * *")

#############################################################################################################################

st.subheader("nan값 제거 후 타겟 표시")
def zero2median(df):
    columns_with_zero = df.columns[data.isna().sum() > 0][1:-1]
    # Index(['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'], dtype='object')
    df[columns_with_zero]=df[columns_with_zero].replace(0,np.nan)
    for feature in columns_with_zero:
        df[feature].fillna(df[feature].median(),inplace=True)
    return df
df = zero2median(data)

df['target'] = df['target'].apply(lambda x: 'DM' if x == 1 else 'noDM')
st.write(df['target'])
st.write(df)
st.markdown("* * *")

#############################################################################################################################

classes=df.target
noDB,DB=classes.value_counts()
st.sidebar.write('non-diabetes(noDM):',noDB)
st.sidebar.write('diabetes(DM):',DB)
st.markdown("* * *")

#############################################################################################################################

st.subheader("상관관계")
if st.checkbox("corr"):
    corr = df.corr(method="pearson")
    st.write(corr)
    plt.figure(figsize=(12,10))
    sns.heatmap(corr, xticklabels=df.columns, yticklabels=df.columns,vmin=-1,vmax=1.0,annot=True)
    st.pyplot()
    df2=df.copy()
    df2 = df2[['age','cp','thalach','exang','oldpeak','slope','ca','thal']]
    corr2 = df2.corr(method="pearson")
    plt.figure(figsize=(12,10))
    sns.heatmap(corr2, xticklabels=df2.columns, yticklabels=df2.columns,vmin=-1,vmax=1.0,annot=True)
    st.pyplot()

if st.button("corr"):
    corr = df.corr(method="pearson")
    st.write(corr)
    plt.figure(figsize=(12,10))
    sns.heatmap(corr, xticklabels=df.columns, yticklabels=df.columns,vmin=-1,vmax=1.0,annot=True)
    st.pyplot()
st.markdown("* * *")

#############################################################################################################################

if st.checkbox("nan"):
    st.write('non-diabetes(noDM):',noDB)
    st.write('diabetes(DM):',DB)

if st.button("nan"):
    st.write('non-diabetes(noDM):',noDB)
    st.write('diabetes(DM):',DB)
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_data")
if st.checkbox("data"):
    st.dataframe(df)

st.subheader("button_data")
if st.button("data"):
    st.dataframe(df)
st.markdown("* * *")
  
#############################################################################################################################

st.subheader("checkbox_bar")
if st.checkbox("bar"):
    df.plot(kind='bar',y=['slope','fbs','cp'])
    plt.legend(loc='upper right')
    st.pyplot()

st.subheader("button_bar")
if st.button("bar"):
    df.plot(kind='bar',y=['slope','fbs','cp'])
    plt.legend(loc='upper right')
    st.pyplot()
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_box")
if st.checkbox("box"):
    df.plot(kind='box',subplots=True,layout=(5,3),sharex=False,sharey=False)
    
    st.pyplot()

st.subheader("button_box")
if st.button("box"):
    df.plot(kind='box',subplots=True,layout=(5,3),sharex=False,sharey=False)
    
    st.pyplot()
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_box2")
if st.checkbox("box2"):
    plt.boxplot(df['sex'])
    
    st.pyplot()

st.subheader("button_box2")
if st.button("box2"):
    plt.boxplot(df['sex'])
    
    st.pyplot()
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_hist")
if st.checkbox("hist"):
    plt.figure(figsize=(12,10))
    data.hist()
    plt.tight_layout()
    st.pyplot()

st.subheader("button_hist")
if st.button("hist"):
    plt.figure(figsize=(12,10))
    data.hist()
    plt.tight_layout()
    st.pyplot()   
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_hist2")
if st.checkbox("hist2"):
    plt.figure(figsize=(12,10))
    data['chol'].hist()
    data['age'].hist()
    plt.tight_layout()
    st.pyplot()

st.subheader("button_hist2")
if st.button("hist2"):
    plt.figure(figsize=(12,10))
    data['chol'].hist()
    data['age'].hist()
    plt.tight_layout()
    st.pyplot()   
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_line")
if st.checkbox("line"):
    
    df["slope"].plot(marker='o',c='r')
    plt.xticks(rotation=90)
    st.pyplot()

st.subheader("button_line")
if st.button("line"):
    df["slope"].plot(marker='o',c='r')
    plt.xticks(rotation=90)
    st.pyplot() 
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_scatter")
if st.checkbox("scatter"):
    plt.rcParams['figure.figsize']=[12,10]
    scatter_matrix(df)
    plt.tight_layout()
    st.pyplot() 

st.subheader("button_scatter")
if st.button("scatter"):
    plt.rcParams['figure.figsize']=[12,10]
    scatter_matrix(df)
    plt.tight_layout()
    st.pyplot() 
st.markdown("* * *")

#############################################################################################################################

st.subheader("checkbox_density")
if st.checkbox("density"):
    df.plot(kind='density',subplots=True,layout=(5,3),sharex=False,sharey=False)
    plt.tight_layout()
    st.pyplot()

st.subheader("button_density")
if st.button("density"):
    plt.rcParams['figure.figsize']=[20,20]
    df.plot(kind='density',subplots=True,layout=(5,3),sharex=False,sharey=False)
    plt.tight_layout()
    st.pyplot()  
st.markdown("* * *")

#############################################################################################################################

if st.checkbox("Skew of attribute distributions"):
        skew = df.skew()
        st.write(skew)
        st.markdown('- 데이터 왜곡도')



