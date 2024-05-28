
import streamlit as st 
from constant import *
import numpy as np 
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
#import tensorflow as tf
from streamlit_player import st_player

st.set_page_config(page_title='Serge Keita\'s portfolio' ,layout="wide",page_icon='👨‍🔬')

st.markdown(info['LinkedIn_profile'],unsafe_allow_html=True)

#st.sidebar.markdown(linkedin_script, unsafe_allow_html=True)

#st.sidebar.markdown(info['test'],unsafe_allow_html=True)

st.header(':green[Data Scientist | Data Engineer | Devops Engineer | Python Developper] ', divider="green",)


########################################### ABOUT ME ####################################################


st.subheader(':green[About me]')
st.write(info['Brief'])



####################################### Career snapshot #################################################


st.subheader(':green[Career snapshot]')
  
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)
        

######################################### Education ###################################################

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.subheader(':green[Education 📖]')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='green',
                align='left',height=50,font_size=20,font_color='black'),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               align='left',height=40,font_size=15))])

fig.update_layout(width=800, height=400)
st.plotly_chart(fig)


######################################### Projects ###################################################

st.subheader(':green[Projects] ')

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

for category, project_list in projects.items():
    with st.expander(category):
        for project in project_list:
            st.markdown(f"### [{project['title']}]({project['link']})")
            st.image(project['image'], width=100)
            st.write(project['description'])



###################################### Skills & Tools ################################################

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.subheader(':green[Skills & Tools ⚒️]')

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()


###################################### Certifications ################################################

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

st.subheader(':green[Certifications]')

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

# Afficher les certifications de manière horizontale
columns = st.columns(len(certifications))

for i, cert in enumerate(certifications):
    with columns[i]:
        st.markdown(f"""
        <div style="text-align: center;">
            <a href="{cert['link']}" target="_blank">
                <img src="{cert['image_url']}" alt="{cert['title']}" style="width: 100px; height: 100px;">
                <p style="font-size: 20px;">{cert['title']}</p>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        

st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: sergekeita01@gmail.com')
st.sidebar.write('📧: +33 698480507')

pdfFileObj = open('pdfs/CV_Serge_Keita.pdf', 'rb')
st.sidebar.download_button('download resume',pdfFileObj,file_name='CV_Serge_Keita.pdf',mime='pdf')



        

        
        
    
    
