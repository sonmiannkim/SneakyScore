import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from data_page import show_data_page
from performance_page import show_performance_page

header = st.container()

with header:
    st.title("Sneaky Score - Score with No Sense!")

page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Data Graphs", "Project Explained", "Performance Explained"))

if page == "Predict" :
    show_predict_page()
elif page == "Data Graphs":
    show_explore_page()
elif page == "Project Explained":
    show_data_page()
else:    
    show_performance_page()

