# -*- coding: utf-8 -*-
"""Graded Assignment 8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SYjQz-IZjVOPZG_zVHQXqINqaPOrCjCg
"""

import streamlit as st

st.set_page_config(page_title="Largest Number Finder", page_icon=":mag:")

def find_largest(a, b, c):
    return max(a, b, c)

# Custom CSS for a nicer look
st.markdown(
    """
<style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f0f2f6;
    }
    .stApp {
        padding: 40px;
    }
    .container {
        padding: 20px;
        background-color: #ffffff;
        margin-bottom: 20px;
    }
    h1 {
        color: #1f77b4;
        font-weight: bold;
    }
    h2 {
        color: #1f77b4;
        font-weight: bold;
    }
    .number-label {
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title('Largest Number Finder')
st.write('Enter three numbers to find the largest among them')

st.markdown('<div class="container">', unsafe_allow_html=True)

with st.form("number_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<p class="number-label">Enter the first number:</p>', unsafe_allow_html=True)
        num1 = st.number_input('', value=0, step=1, key="num1")
    with col2:
        st.markdown('<p class="number-label">Enter the second number:</p>', unsafe_allow_html=True)
        num2 = st.number_input('', value=0, step=1, key="num2")
    with col3:
        st.markdown('<p class="number-label">Enter the third number:</p>', unsafe_allow_html=True)
        num3 = st.number_input('', value=0, step=1, key="num3")

    submit_button = st.form_submit_button("Find Largest Number")

st.markdown('</div>', unsafe_allow_html=True)

if submit_button:
    largest_number = find_largest(num1, num2, num3)
    st.success(f'The largest number is: {largest_number}')