from enum import unique
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
# to aid web displaying drop down


vehicles_df = pd.read_csv("data/web_interact.csv")
vehicles_dummifid_df = pd.read_csv("data/dummified_binned_data.csv")

def get_make() :
    makes = pd.unique(vehicles_df['MAKE'])   
    return makes
 
def get_model(make):
    if " " in make or len(make) == 0:
        models =["Please select Make"]
    else:
        models = pd.unique(vehicles_df['MODEL'][vehicles_df['MAKE']==make])
    return models


def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
#Input params here
regressor = data["model"]



def show_predict_page():    
    st.write("""#### We need information to predict please enter followings """)
    #Two select box - map it to data base
    make=''
    model = ''

    makes = get_make()    
   
    #Min, Max, default
    age = st.slider("Age", 16, 85, 35 )

    gender = st.radio("Gender",["Male", "Female"])

    year = st.selectbox("Vehicle Year", range(2011,2023, 1))

    make = st.selectbox("Vehicle Make", makes, on_change=callback(make))    
    #format_func=lambda x:makes[x], on_change=callback(make)    
    model = st.selectbox("Vehicle Model", get_model(make))

    ok = st.button("Calculate My score")
    if ok:       
        if gender == 'Female':
           gender = 0
        else:
            gender = 1    
        year_col = 'YEAR_' + str(year)
        model_col = 'MAKE_' + make
        model_col = 'MODEL_' + model
        one_table_data = pd.DataFrame(vehicles_dummifid_df.iloc[:1, :])
        one_table_data.drop(columns = ['CREDIT_SCORE', 'SCORE_BUCKET'],axis=1, inplace=True)   
        one_table_data['GENDER'] = gender
        one_table_data['AGE'] = age
        one_table_data[year_col] = 1
        one_table_data[model_col] = 1
        one_table_data[ model_col] = 1
        predicted_score = regressor.predict(one_table_data)
        st.write("""##### The Estimated Credit Score From the DecisionTree is  """ )
        st.subheader(f"{predicted_score[0]:.2f}")
        st.write("""##### What does this score mean?  """ )
        t1 = "<div><span style='color:#2980B9; font-size:14;'>It means that over 260,000 car owners were ran through the DecisionTree algorithm </span></div>"
        t2 = "<div><span style='color:#2980B9; font-size:14;'>to calculate your score and it says your score is as shown. </span></div>"
        st.markdown(t1, unsafe_allow_html=True)
        st.markdown(t2, unsafe_allow_html=True)
        bins = [100, 570, 625, 690, 795, 852, 1000]
        if predicted_score > 5:
            st.write("""##### Excellent! """ )
        elif predicted_score > 4:
            st.write("""##### Very Good! """ )
        elif predicted_score > 3:
            st.write("""##### Good! """ )
        elif predicted_score > 2:
            st.write("""##### Don't go hopping for a while! """ )
        else:
            st.write("""##### Lady! No shopping Allowed! :) """ )

def callback(make):    
    get_model(make)
   
   