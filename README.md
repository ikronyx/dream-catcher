# Text-to-Image Summarizer (Free SaaS MVP)

This app takes a long descriptive text, splits it into 5 parts, summarizes each part, and generates an image for each using free tools.

## 🔧 Stack
- Streamlit (UI)
- T5-small via Hugging Face (Summarization)
- Pollinations API (Image generation)
- nltk (Text splitting)

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## 🌐 Live Demo
You can deploy this free on [Streamlit Cloud](https://streamlit.io/cloud).
