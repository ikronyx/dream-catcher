import streamlit as st
from text_utils import split_text_into_5_parts, summarize_chunk, split_paragraph_by_period
from image_utils import get_pollinations_url
from gen_ai import generate_description

st.set_page_config(page_title="Text-to-Image Summarizer", layout="wide")

st.title("📚 Text-to-Image Summarizer & Generator")
st.markdown("Paste a long text description below. We'll split, summarize, and generate an image for each part.")

user_input = st.text_area("Your Input Text", height=300)

future_goals = st.text_input("What are future goals?")
desires = st.text_input("What are your desires?")

future_goals = "My future goals are: " + future_goals
desires = "My desires are: " + desires

collective_input = future_goals + desires

if future_goals and desires:
    st.text(collective_input)

# if user_input:
#     with st.spinner("Processing..."):
#         parts = split_paragraph_by_period(user_input)
#         # summaries = [summarize_chunk(p) for p in parts]

#         st.header("🖼️ Results")
#         for i, summary in enumerate(parts):
#             image_url = get_pollinations_url(summary)
#             st.subheader(f"Part {i+1}")
#             st.image(image_url, caption=summary)
