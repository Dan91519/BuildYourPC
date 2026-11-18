import streamlit as st

import pandas as pd

from quiz_data import QUIZZES


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

# Show real parts from our CSV for this category
with st.expander("See example parts from our shop"):
    examples = parts[parts["category"] == chosen_key][["name", "price", "note"]]
    st.dataframe(examples, hide_index=True)

# ---------------- QUIZ (one quiz per part) ----------------
st.divider()
questions = QUIZZES[chosen_key]
 
st.subheader(chosen_key + " Quiz")
st.caption(str(len(questions)) + " questions. Pick one answer for each, then check your score.")
 
for i, q in enumerate(questions):
    with st.container(border=True):
        st.radio(
            str(i + 1) + ". " + q["question"],
            q["options"],
            index=None,
            key="quiz_" + chosen_key + "_" + str(i),
        )

if st.button("Check my answers", type="primary", key="check_" + chosen_key):
    score = 0
    for i, q in enumerate(questions):
        if st.session_state["quiz_" + chosen_key + "_" + str(i)] == q["answer"]:
            score = score + 1
 
    st.subheader("Your score: " + str(score) + " / " + str(len(questions)))
    st.progress(score / len(questions))
 
    if score == len(questions):
        st.balloons()
        st.success("Perfect score! You really know your " + chosen_key + ".")
    elif score >= 7:
        st.info("Nice work! Read the review below and try again.")
    else:
        st.warning("Keep going. Read the explanations below and have another go.")
 
    with st.expander("Review every question", expanded=True):
        for i, q in enumerate(questions):
            picked = st.session_state["quiz_" + chosen_key + "_" + str(i)]
            if picked == q["answer"]:
                st.markdown("✅ **" + q["question"] + "**")
            else:
                st.markdown("❌ **" + q["question"] + "**")
            st.caption("Answer: " + q["answer"] + ". " + q["explanation"])
