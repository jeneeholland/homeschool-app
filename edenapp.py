import streamlit as st
from datetime import datetime
import requests
import random
from pokemon_helper import get_daily_pokemon

#### py -m streamlit run edenapp.py --server.address 0.0.0.0 --server.port 8501
#### py -m streamlit run edenapp.py 
#------------------------- PAGE CONFIG ------------------------------------------
# st.set_page_config(
page_title="Homeschool Quest",
page_icon="🌟",
layout="centered"
#------------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
}

.stApp {
    background-color: #ffe6f2;
}

h1 {
    font-size: 3rem !important;
    color: #ff4fa3 !important;
    text-align: center;
    font-weight: 700 !important;
}

h2, h3 {
    color: #6a4cff !important;
    font-weight: 700 !important;
}

p, div, label {
    font-size: 1.1rem !important;
}

.stCheckbox label {
    font-size: 1.2rem !important;
    font-weight: 600 !important;
}

[data-testid="stMarkdownContainer"] {
    font-size: 1.1rem;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)



# ------------------------------------------------------------------------


# Date
today = datetime.now()
date_text = today.strftime("%A, %B %d")

# Weather for Raleigh/Knightdale area
latitude = 35.79
longitude = -78.48

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,weather_code",
    "temperature_unit": "fahrenheit"
}

response = requests.get(url, params=params)
weather = response.json()["current"]

temperature = round(weather["temperature_2m"])
weather_code = weather["weather_code"]

st.title("Homeschool Quest Board")

st.write(f"Today is {date_text}.")
st.write(f"Weather: {temperature}°F")
#----------------------------------------------------------------------------------
st.subheader("🎮 Pokémon Companions of the Day")

daily_pokemon = get_daily_pokemon()

cols = st.columns(3)

for col, pokemon in zip(cols, daily_pokemon):
    with col:
        st.write(f"**{pokemon['name']}**")
        st.image(pokemon["image"], width=150)
        st.write("Type:", ", ".join(pokemon["types"]))
#----------------------------------------------------------------------------------
st.subheader("🎯 Today’s Quests")

math = st.checkbox("Math")
reading = st.checkbox("Spelling")
grammar = st.checkbox("BJU English")
spanish = st.checkbox("Spanish")
science = st.checkbox("Typing")

completed = sum([math, reading, grammar, spanish, science])
st.progress(completed / 5)

st.write(f"You completed {completed} out of 5 quests!")
if completed == 5:
    st.balloons()
    st.success("🎉 Great job, Eden! You completed all your quests today!")