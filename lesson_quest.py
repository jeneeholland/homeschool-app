st.subheader("🎯 Today’s Quests")

math = st.checkbox("Math")
reading = st.checkbox("Spelling")
grammar = st.checkbox("English")
spanish = st.checkbox("Duolingo Spanish")
science = st.checkbox("Typing")

completed = sum([math, reading, grammar, spanish, science])
st.progress(completed / 5)

st.write(f"You completed {completed} out of 5 quests!")
if completed == 5:
    st.balloons()
    st.success("🎉 Great job, Eden! You completed all your quests today!")