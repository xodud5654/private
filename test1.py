import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

## Load data
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Load diabetes data')

data = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")

col_idx = data.columns
row_idx=data.index

data.isna().sum()
description = data.describe()
class_counts = data.groupby('Outcome').size() 
v,c=np.unique(data['Outcome'], return_counts=True)

correlations = data.corr(method = 'pearson')

fig, ax = plt.subplots(1,1,figsize=(10,8))
img = ax.imshow(correlations,cmap='coolwarm',interpolation='nearest')  
ax.set_xticklabels(data.columns)
plt.xticks(rotation=50)
ax.set_yticklabels(data.columns)
fig.colorbar(img)
fig.tight_layout()
plt.show()
st.pyplot()

st.markdown("* * *")

skew = data.skew()
data.hist()
fig.tight_layout()
plt.show()
st.pyplot()

st.markdown("* * *")

data.plot(kind='density', subplots=True, layout=(3,3), sharex=False) # -> x축 공유 X
fig.tight_layout()
plt.show()
st.pyplot()

st.markdown("* * *")

data.plot(kind= 'box', subplots=True, layout=(3,3), sharex=False, sharey=False)
fig.tight_layout()
plt.show()
st.pyplot()

st.markdown("* * *")

correlations = data.corr(method = 'pearson')

import seaborn as sns

plt.plot(figsize=(10,8))
sns.heatmap(correlations, 
        xticklabels=data.columns, 
        yticklabels=data.columns,
        vmin= -1, vmax=1.0)
fig.tight_layout()
plt.show()
st.pyplot()

st.markdown("* * *")

from pandas.plotting import scatter_matrix  
plt.rcParams['figure.figsize'] = [10, 12]
scatter_matrix(data)
fig.tight_layout()
plt.show()
st.pyplot()

st.markdown("* * *")

sns.pairplot(data)
fig.tight_layout()
st.pyplot()