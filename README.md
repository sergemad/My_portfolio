# Portfolio builder

A streamlit based webapp 

## Contents

- LinkedIn Badge : [how to create one for your profile?](https://www.linkedin.com/pulse/how-create-linkedin-badge-your-website-amy-wallin/). Integrated using streamlit component
- Career Snapshot: Built using [streamlit_timeline](https://pypi.org/project/streamlit-timeline/)
- Skills & Tools: Used streamlit buttons & columns features
- Education : Plotly(library for visualization) table

## Files description
* images/ : images used for the portfolio
* pdf/ : pdfs available for downloading on portfolio
* constant.py : File with all static data used. 
* requirements.txt : requirements file generated using
* timeline.json : Json file used by streamlit_timeline for career snapshot

## How to deploy using Streamlit?
* Once confirm your app runds fine on localhost. Check using 
```
streamlit run Portfolio.py 
```
* Create requirements.txt. 
* Push repo to github.
* Sign in https://streamlit.io/ using the same mail as for github account where code is pushed (for ease)
* Fill in the info & click deploy on the !

