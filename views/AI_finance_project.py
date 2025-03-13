import streamlit as st

# --- Title ---
st.title("💲 Personal AI-Powered Financial Analysis with LLaMA and AutoGPT Integration")

# --- Overview Section ---
st.header("📌 Overview")
st.write(
    """
    This AI-driven platform integrates **LLaMA** and **AutoGPT** to autonomously perform **financial, cybersecurity, and market analysis**.
    The system operates in a **client-server architecture**, allowing for high-volume **web scraping, NLP (Natural Language Processing), 
    and cybersecurity insights aggregation**. The final output consists of **automated, actionable reports** generated at various timeframes 
    (e.g., weekly, monthly, yearly).
    """
)

# --- Key Features ---
st.header("🔹 Key Features")
st.markdown(
    """
    - 🔍 **NLP-Powered Insights**: Multi-source datasets, sentiment analysis, and risk assessments for data-driven decision-making.  
    - 🤖 **AutoGPT Integration**: Operates **without external APIs**, ensuring **data privacy** and **full autonomy**.  
    - 📜 **Cybersecurity Document Ingestion**: Supports **tokenized, preprocessed PDFs** for cybersecurity best practices.  
    - 📈 **Financial Sentiment Analysis**: Evaluates **market trends** and **risk factors** using machine learning models.  
    """
)

# --- Achievements ---
st.header("🏆 Achievements")
st.markdown(
    """
    - ⚡ **Performance Optimization**: Reduced **response time** from **~526 seconds to 113 seconds** by optimizing **CPU threading** and leveraging **selective GPU acceleration**.  
    - 🛠️ **Efficient Memory Management**: Solved **memory bottlenecks** by implementing **CPU/GPU balancing, error logging, and iterative debugging**.  
    - 🔄 **Improved Model Accuracy**: Enhanced **financial predictions** by incorporating multiple **fine-tuned transformer models**.  
    """
)

# --- Technical Challenges ---
st.header("🛠️ Technical Challenges")
st.markdown(
    """
    - 🔧 **Debugging Memory Constraints**: Identified and resolved **CPU/GPU allocation issues**.  
    - 📊 **Data Pipeline Optimization**: Improved **data ingestion, feature engineering, and fine-tuning workflows**.  
    - 🐧 **Linux-Based Optimization**: Ensured **smooth operation** in a **Linux environment**, addressing **performance inconsistencies**.  
    """
)

# --- Sample Debug Log ---
st.header("📝 Sample Debug Log")
st.code(
    """
    2024-10-28 13:37:47 - INFO - Received POST request for prompt: "Hello, LLaMA."
    2024-10-28 13:38:02 - INFO - CUDA Memory: Usage at 95%, rebalancing to CPU.
    2024-10-28 13:40:15 - INFO - Response generated in 113 seconds.
    """, language="plaintext"
)

# --- Sample Code Snippet ---
st.header("💻 Sample Code Snippet")
st.code(
    """
import os
import json
import torch
import logging
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split

# File Paths
data_path = "/home/ecks/PycharmProjects/auto_gpt/llama_env/data/repaired_data.json"
log_path = "/home/ecks/PycharmProjects/untitled/fine_tuning_log.txt"

# Load Model and Tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Function for Financial Sentiment Analysis
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    sentiment_score = torch.nn.functional.softmax(outputs.logits, dim=1)
    return sentiment_score

# Example Analysis
example_text = "Tech stocks are rising after strong earnings reports."
sentiment_result = analyze_sentiment(example_text)
print(f"Sentiment Analysis Result: {sentiment_result}")
    """, language="python"
)

