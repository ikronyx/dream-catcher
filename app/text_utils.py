import nltk
from nltk.tokenize import sent_tokenize
from transformers import pipeline

nltk.download('punkt')  # only needs to run once
summarizer = pipeline("summarization", model="t5-small")

def split_text_into_5_parts(text):
    sentences = sent_tokenize(text)
    k = len(sentences) // 5 or 1
    chunks = [sentences[i*k:(i+1)*k] for i in range(5)]
    return chunks

def summarize_chunk(chunk_sentences):
    text = ' '.join(chunk_sentences)
    summary = summarizer(text, max_length=25, min_length=5, do_sample=False)
    return summary[0]['summary_text']

def split_paragraph_by_period(paragraph):
    raw_sentences = paragraph.split('.')
    sentences = [s.strip() for s in raw_sentences if s.strip()]
    return sentences
