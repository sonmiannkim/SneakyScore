from enum import unique
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import seaborn as sns
import streamlit.components.v1 as components

def plot_corr(df, size=10):
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.legend()
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
    plt.yticks(range(len(corr.columns)), corr.columns)

@st.cache 
def load_data():
    df = pd.read_csv("data/driver_vehicle.csv") 
    
    df = df[['AGE', 'CREDIT_SCORE','GENDER', 'MAKE']]   
    return df

df = load_data()

def show_explore_page():  
      
    st.write(
        """
        ### Vehicle vs Credit Score Mean Bar Chart
        """
    )
    data = df.groupby(['MAKE'])['CREDIT_SCORE'].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.write(
        """
        ### Vehicle vs Age Mean Line Chart
        """
    )
    data = df.groupby(['MAKE'])['AGE'].mean().sort_values(ascending=True)
    st.line_chart(data)

    drivers_df = pd.read_csv("data/driver_vehicle.csv")
    st.write(
        """
        ### Data by car maker
        """
    )
    data_dist = pd.DataFrame(drivers_df['MAKE'].value_counts())
    st.bar_chart(data_dist)

    st.write(
        """
        ### Feature correlation Heat Map
        """
    )
    fig, ax = plt.subplots()
    sns.heatmap(drivers_df.corr(), ax=ax)
    st.write(fig)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,10))
    drivers_df.plot(kind='hist', y='CREDIT_SCORE', bins=2, color='b', ax=axes[0][0])   
    drivers_df.plot(kind='hist', y='GENDER', bins=5, color='r', ax=axes[0][1])
    drivers_df.plot(kind='hist', y='AGE', bins=range(10, 100, 10), color='g', ax=axes[1][0])
    results_df = pd.read_csv("data/score_results.csv") 
    results_df.plot(kind='hist', y='ESTIMATED', bins=10, color='orange', ax=axes[1][1])
    st.write(fig)