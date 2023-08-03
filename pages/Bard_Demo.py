import streamlit as st
from bardapi import Bard
import os
import requests
import pandas as pd


st.title("Bard API Demo with Streamlit")
st.write("Enter a question below to get an answer from the Bard API.")


# Streamlit user input
input_text = st.text_input("Enter your question:", "Why did Tesla stock go up over the past year?")


# Send an API request and get a respons
bard_output = Bard().get_answer(input_text)['content']
st.write(bard_output)


# Generate another output from Bard
input_text_2 = "what is chatgpt?"
bard_output_2 = Bard().get_answer(input_text)['content']

# Create a dataframe with Input and Output columns
df = pd.DataFrame(columns=["Input", "Output"])

st.write(df)
# Create new rows as dataframes with the reponses
new_row = pd.DataFrame({"Input": [input_text], "Output": [bard_output]})
new_row1 = pd.DataFrame({"Input": [input_text_2], "Output": [bard_output_2]})

# Append the new rows to the existing dataframe
df = pd.concat([df, new_row], ignore_index=True)
df = pd.concat([df, new_row1], ignore_index=True)

# Print the dataframe
st.write(df)
