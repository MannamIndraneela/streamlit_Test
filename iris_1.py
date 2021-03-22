import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

name= st.text_input("User Name", "Indra Neela")
file= st.file_uploader("select a file")
click= st.button("submit")
if(click == True):
    st.write("Output 1 - Top 5 rows of the data frame")
    df= pd.read_csv("iris.csv")
    df.head()
    st.write(df.head())


    st.write("Output 2 - Display the scatter plot between petal_length and sepal_length")
    fig = plt.figure()

    plt.scatter(df["petal_length"],df["sepal_length"])

    plt.xlabel("Petal Length")
    plt.ylabel("Sepal Length")

    st.write(fig)
