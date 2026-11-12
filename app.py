import streamlit as st

import pandas as pd

st.set_page_config(page_title="Build Your PC", page_icon="🖥️", layout="wide")

parts = pd.read_csv("components.csv")

from component_info import COMPONENTS
 
st.title("Learn PC Parts")
st.write("Pick a part below and discover what it does.")
 
# One button per part: "CPU", "GPU", "RAM" ...
chosen_key = st.radio("Choose a part:", list(COMPONENTS.keys()), horizontal=True)
info = COMPONENTS[chosen_key]
 
st.header(info["emoji"] + " " + info["title"])
st.subheader(info["short"])
 
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("**Easy way to think about it**")
        st.write(info["analogy"])
    with st.container(border=True):
        st.markdown("**Fun fact**")
        st.write(info["fun_fact"])
with col2:
    with st.container(border=True):
        st.markdown("**What to look for**")
        for tip in info["look_for"]:
            st.markdown("- " + tip)
