# story_helper.py

import streamlit as st
from google import genai

def make_pokemon_story(pokemon_names):
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"]) # uses GEMINI_API_KEY from your environment

    prompt = f"""
    Write a short, fun, age-appropriate story for a 9-year-old.

    Include these 3 Pokémon:
    {", ".join(pokemon_names)}

    Rules:
    - Keep it under 200 words.
    - Make it kind, adventurous, and easy to understand.
    - Include a gentle lesson about teamwork or courage.
    - Do not include anything scary or inappropriate.
    """

    response = client.models.generate_content(
        #model="gemini-3-flash-preview",
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text