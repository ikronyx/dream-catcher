import streamlit as st
from text_utils import split_text_into_5_parts, summarize_chunk, split_paragraph_by_period
from image_utils import get_pollinations_url
from gen_ai import generate_description

st.set_page_config(page_title="Dream Catcher", layout="wide")

st.title("Imagine a day in your future")

future_goals = st.text_input("What are future goals?", placeholder="e.g., Start a design studio in Bali, run a marathon, publish my novel")
with st.expander("See Examples"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
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

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Take Me There', on_click=click_button, use_container_width=True, type="primary")

if st.session_state.clicked:
    if future_goals and desires:
        story = generate_description(collective_input)
        st.text(story)
