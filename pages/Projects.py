import pandas as pd
import streamlit as st
import os
from constant import *


st.markdown(info['LinkedIn_profile'],unsafe_allow_html=True)

st.header('Projects')


for category, project_list in projects.items():
    with st.expander(category):
        for project in project_list:
            st.markdown(f"### [{project['title']}]({project['link']})")
            st.image(project['image'], width=100)
            st.write(project['description'])