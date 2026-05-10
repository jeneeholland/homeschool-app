

import random

quotes = [
    "Be kind even when it's hard.",
    "Mistakes help us learn and grow.",
    "Teamwork makes every adventure better.",
    "Every expert was once a beginner.",
    "You are stronger than you think.",
    "Small steps lead to big progress.",
    "Good friends help each other grow.",
    "Curiosity is a superpower.",
    "Learning something new takes courage.",
    "Practice helps your skills level up.",
    "A positive attitude can change your whole day.",
    "Helping others makes you stronger too.",
    "It's okay to ask questions.",
    "Patience helps great things to happen.",
    "Trying again is part of success.",
    "Your ideas matter.",
    "Adventure begins with curiosity.",
    "Believe in yourself like Pikachu believes in Ash.",
    "Every trainer starts somewhere.",
    "Even small Pokémon can do big things."
]

def get_daily_quote():

    daily_quote = random.choice(quotes)

    return daily_quote