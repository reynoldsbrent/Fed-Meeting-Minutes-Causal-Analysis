import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from PyPDF2 import PdfReader 
import fitz
import os


# Initialize the sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Initialize empty lists to store sentiments and file names
sentiments = []
file_names = []

directory = "C:\\Users\\brent\\OneDrive\\Documents\\python_projects\\Fed-Meeting-Minutes-Causal-Analysis\\Statements"

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
        
    for page in doc:
        text += page.get_text()
    return text

# Iterate through PDFs in the directory
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        file_path = os.path.join(directory, filename)
        
        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(file_path)
        
        # Analyze sentiment
        sentiment = sia.polarity_scores(pdf_text)
        sentiments.append(sentiment['compound'])
        file_names.append(filename)

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(file_names, sentiments, marker='o')
plt.title('Sentiment Analysis of Federal Reserve Statements')
plt.xlabel('PDF File')
plt.ylabel('Sentiment Score')
plt.xticks(rotation=90)
plt.grid(True)

plt.tight_layout()
plt.savefig('sentiment_chart.png')
plt.show()