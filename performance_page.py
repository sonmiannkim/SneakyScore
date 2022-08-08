from operator import index
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from math import sqrt 

def show_performance_page():    
    dataset= st.container()
    model_training = st.container()
 
    with dataset:   
        st.subheader("All dummified data preview")    
        dummified = pd.read_csv('data/dummified_binned_data.csv')
        dummified = dummified.drop(['CREDIT_SCORE'], axis = 1)
        input_data = pd.DataFrame(dummified.iloc[:1, :])
        input_data.drop(columns = ['SCORE_BUCKET'],axis=1, inplace=True)        
        st.write(dummified.head())     
 
    with model_training:
        st.subheader("Time to train the model Using RandomForestRegressor!")       
        # Assing X and y
        X = dummified.drop(['SCORE_BUCKET'], axis = 1)
        y = dummified.SCORE_BUCKET
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        st.text('In this project, I looked into the Insurance applications and I was curious if car ownership can reflecting  the financial status.')
        sel_col, disp_col = st.columns(2)
        max_depth = sel_col.slider('What should be teh Max_deth?', min_value=5, max_value=50, value=5, step = 5)
        n_estimators = sel_col.selectbox('How many trees?', options=[5, 10, 15, 20], index=0)        
        regr = RandomForestRegressor(max_depth=max_depth, n_estimators = n_estimators)
        regr.fit(X_train, y_train) 
        input_data = pd.DataFrame(dummified.iloc[:1, :]) 
        input_data=input_data.drop(['SCORE_BUCKET'], axis = 1)       
        prediction = regr.predict(input_data)
        y_train_rate = regr.predict(X_train)
        y_test_rate = regr.predict(X_test)
        st.text("Training Accuracy for Random Forest Regression Model (R2 Score):")
        st.write(r2_score(y_train, y_train_rate))

        st.text("Testing Accuracy for Random Forest Regression Model (R2 Score):")
        st.write(r2_score(y_test, y_test_rate))

        st.text("RMSE for Training Data (Root Mean Square Error):")
        st.write(sqrt(mean_squared_error(y_train, y_train_rate)))

        st.text("RMSE for Testing Data (Root Mean Square Error):")
        st.write(sqrt(mean_squared_error(y_test, y_test_rate)))

        st.subheader("The R2 Score explained")
        st.write(
        """
        R2 (R-squared) score is a statistical measure that represents the proportion over the variance of the dependent
        The variable that's explained by an independent variable or variables in a regression model. It is a ratio made between
        Unexplained Variation over Total Variation.  Interestingly our data showed  a similar ratio of Unexplained variation over 
        Total variation, meaning the computed values are very small. Could be understood as the data is consistent.
        """
        )
        st.subheader("The RMSE (Root Mean Square Error) explained")
        st.write(
        """
        RMSE is the standard deviation of the residuals (prediction errors). Residuals are a measure of how far
        from the regression line, data points are. It tells you how concentrated data is around the line of best fit. In these experiments, 
        it wasn't resulting in good measure because the data isn't progressive nor historical. But it is a tool for the statistical analysis
        so I added them here.  This outcome can be computed with the different models running and give us the best fit model for the data set. My choice
        was either Decision Tree or Random Forest (1.21) because the outcome was better than multiple linear (2.24).
        """
        )
        




      