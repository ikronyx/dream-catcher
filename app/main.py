import streamlit as st
from text_utils import split_text_into_5_parts, summarize_chunk, split_paragraph_by_period
from image_utils import get_pollinations_url
from gen_ai import generate_description

st.set_page_config(page_title="Dream Catcher", layout="wide")

st.title("Imagine a day in your future")

future_goals = st.text_input("What are future goals?")
desires = st.text_input("What are your desires?")
look_like = st.text_input("How do want your life to look like?")
to_have = st.text_input("What you want to have?")
want_to_be = st.text_input("How do you want to be?")

future_goals = "My future goals are: " + future_goals
desires = "My desires are: " + desires
look_like = "I want my life to look like: " + look_like
to_have = "I want to have " + to_have
want_to_be = "I want to be like " + want_to_be

collective_input = future_goals + desires

st.markdown("""
    <style>
    .red-button {
        display: block;
        width: 100%;
        padding: 0.75em;
        background-color: #e63946;
        color: white;
        font-size: 1.1em;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        margin-top: 1em;
    }
    .red-button:hover {
        background-color: #d62828;
    }
    </style>
    <button class="red-button" type="submit">Take Me There</button>
""", unsafe_allow_html=True)


# story = generate_description(collective_input)
# st.text(story)
