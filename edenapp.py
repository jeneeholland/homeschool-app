import streamlit as st
from datetime import datetime
import requests
import random
from pokemon_helper import get_daily_pokemon

#### py -m streamlit run edenapp.py --server.address 0.0.0.0 --server.port 8501
#### py -m streamlit run edenapp.py 
#------------------------- PAGE CONFIG ------------------------------------------
# st.set_page_config(
page_title="Eden's Homeschool Quest",
page_icon="🌟",
layout="centered"
#------------------------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #ffd6eb;
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

st.title("Eden's Homeschool Quest Board")

st.write(f"Today is {date_text}.")
st.write(f"Weather: {temperature}°F")
#----------------------------------------------------------------------------------
st.subheader("🎮 Pokémon Companion of the Day")

pokemon_name, pokemon_image = get_daily_pokemon()

st.write(f"Today's Pokémon is: **{pokemon_name}**!")
st.image(pokemon_image, width=200)
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