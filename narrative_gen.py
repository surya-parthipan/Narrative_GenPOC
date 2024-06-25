
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  25 13:30:21 2024

@author: Parthipan R
"""

import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
claude_key = os.getenv("claude_key")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=claude_key)

# Layout and styling
st.set_page_config(page_title="GenAI", layout='wide')
st.title("Narrative Generator")

# Dropdown menu for cities
cities = ["Paris", "London", "New York", "Tokyo", "Sydney"]
selected_city = st.selectbox("Select a city", cities)

if st.button("Generate Narrative"):    
    message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="you're a narrative generator for a tour company.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Give me a narrative for a {selected_city} trip. Give me just the narrative; don't add the headings. Also, limit it to 250 to 500 characters."
                }
            ]
        }
    ]
    )
    
    narrative = message.content[0].text
    st.text_area("Generated Narrative", value=narrative, height=200)

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
    }
    </style>
    """, unsafe_allow_html=True)

# Footer
footer_html = """
<div style='position: fixed; bottom: 0; width: 100%; text-align: center; font-size: 12px;'>
    <hr style='border-color: #F0F2F6;'>
    <p>Developed by 🧑‍💻 Parthipan Ramakrishnan</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)