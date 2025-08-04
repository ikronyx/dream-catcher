import google.generativeai as genai
import os

# api_key_value = open("api_key.txt", 'r', encoding='utf-8').read().strip()

genai.configure(api_key="AIzaSyBfKkPK9DrZYnNn37qiT9P7KAajevp_BQo")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_description(collective_input):
    response = model.generate_content("\'" + collective_input + "\' " + "Tell me a story of a day in the life after I achieve these")
    return response.text