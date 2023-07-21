

from langchain.llms import OpenAI
import os
import streamlit as st
import pandas as pd

llm = OpenAI(temperature=0)

@st.cache
def webpilot(input):
    # Generate a response
    prompt = 'Using WebPilot, give me the historical revenue in euro from this page as a json' + input
    return llm(prompt)

def graph(input):
    # Generate a response
    prompt = 'based on this dataframe plot a bar plot using daigr.am' + input
    return llm(prompt)
# Page title
st.title("WebPilot Revenue Viewer")

# Input URL
input_url = 'https://finance.yahoo.com/quote/LHV1T.TL/financials?p=LHV1T.TL'

# Retrieve historical revenue
response_json = webpilot(input_url)
df = pd.read_json(response_json)

# Display DataFrame
st.write("Historical Revenue Data:")
st.dataframe(df)
st.write(graph(webpilot(input_url)))