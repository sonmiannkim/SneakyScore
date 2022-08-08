from operator import index
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from math import sqrt 
def show_data_page():
    
    dataset= st.container()
    features = st.container()  
    with dataset:
        st.header("Purpose and Motivation")
        st.subheader('Purpose')
        st.write(
        """
        Frankly Speaking, I really didn't know what I was doing in the beginning and I don't 
        fully grasp what I've done it.  I just wanted to grab something and run it and see what it does. 
        My purpose was learning and I was focusing on the subject I wanted.

        """
        )
        st.subheader('Motivation')
        st.write(
        """
        I see many people think that someone with a good car means he/she has a strong financial foundation in order to have one.
        In this project, I really wanted to know if the thoughts can be proved by some numbers by examining the data that I dealt with daily.
        Well, there was another hidden motivation as well though.  The project was approaching its due and I wasn't able to find any 
        satisfying data (I Spent 3 days researching) and I was exhausted googling and clicking websites while I have bunch of data sitting in 
        my computer.  So I thought I could utilize what I have.  Now that was thought as well. 

        """
        )
        st.subheader("Dummified Data")
        dummified = pd.read_csv('data/dummified_binned_data.csv')
        input_data = pd.DataFrame(dummified.iloc[:1, :])
        input_data.drop(columns = ['CREDIT_SCORE', 'SCORE_BUCKET'],axis=1, inplace=True)         
        st.write(dummified.head())
        st.write(
        """
        Initial Features: Initially I had IDs on both tables, and since I thought those IDs can represent individuals, like a drivers ID (thinking there are no duplicates), 
        Vehicles thinking, they are one to many relationships and unique id to represents an individual or a car. Also, since there are many duplicates 
        (count it as a quantity of it), thought it would greatly attribute the facts to the Credit score.    Middle of the project, TA advise me they are independent 
        and treated it as independent variables which would be treated as dummies. 
   
        """
        )         

    with features:
        st.header("What did I learn")
        st.write(
        """
        ###### 1. Different statistical Anayysis
        """
        )
        st.write(
        """
        My exmaple here is RMSE, and R2 score. I read many more, some I understood, some I didn't.  
        However, I learned something I didn't know for details, that was enough for me.
        """
        )

        st.write(
        """
        ###### 2. How are dummy Variales used in Machine Learning
        """
        )
        st.write(
        """
        It broke my first idea of ID issues.  So I will never forget.  The key here is independent.  The independent categorical variables 
        that have no quantifiable relationship with each other, which in my project, it was vehicle properties.
        """
        )
        st.write(
        """
        ###### 2. Different Models
        """
        )
        st.write(
        """
        I am sure there are countless, but Linear, Logistic, Multivariate, Polynomial, thery Logistic, Random Forest
        and the my favorite Decision Tree are few I tried and see what it does and how it works. While testing it, it is just slight different
        one after another and thought there gotta be a way accumulate it all and automatize the process. Is  this mean I still have a job?
        Probably not then.  
        """
        )
        st.write(
        """
        ###### 3. Different Ways of handling the data
        """
        )
        st.write(
        """
        My example here like Gender, can be either dummified or binarize the data, Which I chose latter.
        Also, using K-mean and bucketing by it vs binning it by social acknowleged categories, such as credit score. Both can be doable, but thought
        latter might be more usful. In addition, null filters and out of range removers by condition and much more, cool to play with python 
        provided methods.
        """
        )
        st.write(
        """
        ###### 4. Using web with models 
        """
        )
        st.write(
        """
        I Spent quite sometime understanding why Flask was popular in ML community,but it was very difficult for me 
        at first because of the PKL format (byte streamed object) file.  Out of site, out of understaning its process, for me that was.
        Then I experienced streamlit, which was simple and easy to adopt the PKL formatted file, but it isn't easy otherwise.
        The most difficulty of it was not able to use CSS (although I read an example, but it wasn't work for me). Probably that's why
        the shared public site offers conatinerized sets to cover things you can't manually. Another difficult was not able to use JavaScript
        freely.  Although there are bunch built in, like slider, but still web neeed someting delicate touch.
        """
        )
        st.write(
        """
        ###### 5. While working on this project, I loved ah-ha moments. 
        """
        )
        st.write(
        """
        The reason why I wanted to enroll the school for. Learning something 
        makes you say ah-ha.  I am not sure what I will learn from here, but it provided me good foundation of learning about ML.
        I'd love to use it if I could, but I am not sure if I can get a good job with this.  Even if I don't gain
        a future job with it, I am 100% sure I will have fun with with it still.  Cudos!  Me!
        """
        )
       

    

        




      