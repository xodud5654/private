import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Sidebar
    st.sidebar.header("About -")
    st.sidebar.info("pdm04_st_Mid_exam")

    # Title
    st.title("Mid exam - pdm04, 김채영")
    st.header("- EDA of Pima diabetes data -")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Get the data from github
    df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")

    st.dataframe(df)

    # Return dataframe
    if st.checkbox("Show Data description"):
        st.dataframe(df.describe())
        # shape
        st.subheader("shape")
        df.shape

        #
        st.subheader("Check & cleaning data")
        df.isnull().values.any(), df.isna().sum()

        vars = df.columns
        st.write(vars)
        df = df[vars].dropna()
        df.shape

    if st.checkbox("Skew of attribute distributions"):
        skew = df.skew()
        st.write(skew)
        st.markdown('- 데이터 왜곡도')

    st.markdown("* * *")

    #
    st.header("- Visualizing data -")

    #
    st.subheader("Check the balance of classes in the data through plot")
    if st.checkbox("Outcome plot"):
        classes=df.Outcome
        sns.countplot(classes, label='count')
        st.pyplot()
        nDB,DB=classes.value_counts()
        st.write('False: non-diabetes',nDB)
        st.write('True: diabetes',DB)

        classes.value_counts(), type(classes)
        st.text("0 : 정상인, 1 : 당뇨병 환자")

    st.markdown("* * *")

    #
    st.subheader("Show the data as a chart")
    if st.checkbox("chart"):
        st.line_chart(df)
    
    st.markdown("* * *")

    #
    st.subheader("Univariate plots:")

    #
    if st.checkbox("Histograms"):
        st.subheader("Histograms")
        plt.rcParams['figure.figsize'] = [12, 10] # set the figure size 
        st.write(df.hist())
        st.pyplot()
    
    if st.checkbox("Density Plots"):
        st.subheader("Density Plots")
        st.write(df.plot(kind='density', subplots=True, layout=(3,3), sharex=False))
        st.pyplot()

    if st.checkbox("Box and Whisker Plots"):
        st.subheader("Box and Whisker Plots")
        st.write(df.plot(kind= 'box', subplots=True, layout=(3,3), sharex=False, sharey=False))
        st.pyplot()

    st.markdown("* * *")

    #
    st.subheader("Multivariate Plots:")

    #
    if st.checkbox("Correlation plot"):
        st.subheader("Correlation plot")
        df.corr()
        plt.figure(figsize=(12,10))
        sns.heatmap(df.corr(),annot=True, cmap= "RdYlGn", vmin=-1, vmax=1)
        st.pyplot()
    
    if st.checkbox("Compute correlation matrix"):
        st.subheader("Correlations of attributes in the data")
        correlations = df.corr(method = 'pearson')
        st.write(correlations)
        st.markdown('- 값이 1에 가까울수록 상관성이 있음!')
    
    if st.checkbox("result"):
        st.markdown('- 상관성 분석 결과\n'
            '   * Age vs. Pregnancies : 0.54\n'
            '   * Glucose vs. Outcome : 0.47\n'
            '   * SkinThickness vs. Insulin : 0.44\n'
            '   * SkinThickness vs. BMI : 0.39\n')
        st.markdown('- 상관성이 높은 변수들에 대한 좀 더 자세한 시각화가 필요하다.')

    st.markdown("* * *")

    #
    # Import required package 
    from pandas.plotting import scatter_matrix
    plt.rcParams['figure.figsize'] = [12, 12]

    if st.checkbox("Scatter Plot Matrix"):
        st.subheader("Scatter Plot Matrix")
        scatter_matrix(df)
        plt.show()
        st.pyplot()

    if st.checkbox("Scatter Plot_1"):
        st.subheader("Scatter Plot")
        sns.pairplot(df, hue="Outcome", markers=["o", "s"],palette="husl")
        st.pyplot()

    if st.checkbox("Scatter Plot_2"):
        st.subheader("0, 1을 noDM, DM으로 변경")
        df_temp = df.copy()
        df_temp['Outcome'] = df_temp['Outcome'].replace([0, 1],['noDM', 'DM'])
        sns.pairplot(df_temp, hue='Outcome', markers=["o", "s"],palette="husl")
        st.pyplot()

    st.markdown("* * *")

    #
    if st.checkbox("6 high correlation"):
        st.subheader("상관성이 높은 6개의 특성에 대한 산포도")
        high_corr = ['Pregnancies', 'Glucose', 'SkinThickness', 'Insulin', 'BMI','Age', 'Outcome']
        df_temp2 = df.copy()
        df_temp2['Outcome'] = df_temp2['Outcome'].replace([0, 1],['noDM', 'DM'])
        sns.pairplot(df_temp2[high_corr], hue='Outcome')
        st.pyplot()
    
    if st.checkbox("3 high correlation"):
        st.subheader("상관성이 높은 3개의 특성에 대한 산포도")
        highest_corr = ['Pregnancies', 'Age', 'Outcome']
        df_temp3 = df.copy()
        df_temp3['Outcome'] = df_temp3['Outcome'].replace([0, 1],['noDM', 'DM'])
        sns.pairplot(df_temp3[highest_corr], hue='Outcome')
        st.pyplot()

    st.markdown("* * *")

    #
    st.subheader("Advanced plots:")

    #
    if st.checkbox("Standarization of data and Violinplot"):
        st.markdown('- Standarization of data (Normalization)')
        df_n = (df - df.mean())/df.std()
        df_n

        y=df.Outcome
        df2=pd.concat([y, df_n.iloc[:,0:8]], axis=1)
        y.shape,df2.shape

        df3=pd.melt(df2,id_vars='Outcome', var_name='features',value_name='values')
        df3.head(), df3.shape
        
        st.subheader("Violinplot")
        plt.figure(figsize=(10,10))
        sns.violinplot(x='features', y='values', hue='Outcome', data=df3, split=True, inner='quart')
        plt.xticks(rotation=45)
        st.pyplot()

        #
        if st.checkbox("Customizing seaborn plot"):
            st.subheader("Customizing seaborn plot")
            sns.set(style='whitegrid', palette='muted')
            plt.figure(figsize=(10,10))
            sns.swarmplot(x='features', y='values', hue='Outcome', data=df3)
            plt.xticks(rotation=45)
            st.pyplot()

    st.markdown("* * *")

if __name__ == '__main__':
	main()