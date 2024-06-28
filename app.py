import bs4 as bs
import urllib.request as url
import re
import nltk
import heapq
import matplotlib.pyplot as plt
import streamlit as st
from string import punctuation

nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape the webpage
def get_webpage(url_address):
    data = url.urlopen(url_address)
    article = data.read()
    parsed_article = bs.BeautifulSoup(article, 'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text = " ".join([p.text for p in paragraphs])
    return article_text

# Function to clean the text
def text_cleaning(text):
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    formatted_text = re.sub('[^a-zA-Z]', ' ', text)
    formatted_text = re.sub(r'\s+', ' ', formatted_text)
    return text, formatted_text

# Function to tokenize and remove stopwords
def tokenize_and_remove_stopwords(text):
    stopwords_list = nltk.corpus.stopwords.words('english')
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.lower() not in stopwords_list and word not in punctuation]
    return words

# Function to calculate word frequencies
def calculate_word_frequencies(words):
    word_frequencies = {}
    for word in words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    return word_frequencies

# Function to normalize word frequencies
def normalize_frequencies(word_frequencies):
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequency
    return word_frequencies

# Function to score sentences
def score_sentences(sentences, word_frequencies):
    sentence_scores = {}
    for sent in sentences:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores:
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    return sentence_scores

# Function to generate summary
def generate_summary(sentence_scores, num_words):
    summary_sentences = heapq.nlargest(len(sentence_scores), sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    words = summary.split()[:num_words]
    summary = ' '.join(words)
    return summary

# Function to extract most important words
def most_important_words(word_frequencies, n=30):
    most_important_words = heapq.nlargest(n, word_frequencies, key=word_frequencies.get)
    return most_important_words

# Function to run the summarization
def summarize_webpage(url_address, num_words):
    article_text = get_webpage(url_address)
    cleaned_text, formatted_text = text_cleaning(article_text)
    sentences = nltk.sent_tokenize(cleaned_text)
    words = tokenize_and_remove_stopwords(formatted_text)
    word_frequencies = calculate_word_frequencies(words)
    word_frequencies = normalize_frequencies(word_frequencies)
    sentence_scores = score_sentences(sentences, word_frequencies)
    summary = generate_summary(sentence_scores, num_words=num_words)
    important_words = most_important_words(word_frequencies)
    return summary, important_words, word_frequencies

# Streamlit UI
st.title("Webpage Summarizer")

# Enter URL
url_address = st.text_input("Enter URL:")

num_words = st.number_input("Number of words:", min_value=1, step=1)

if st.button("Summarize"):
    if url_address:
        summary, important_words, word_frequencies = summarize_webpage(url_address, num_words=num_words)
        
        st.subheader("Most Important Words:")
        st.write(", ".join(important_words))
        
        st.subheader("Word Frequency Distribution:")
        # Plot the word frequency distribution
        freq_dist = nltk.FreqDist(word_frequencies)
        plt.figure(figsize=(10, 6))
        freq_dist.plot(30, cumulative=False)
        st.pyplot(plt)

        st.subheader("Summary:")
        st.write(summary)
    else:
        st.write("Please enter a valid URL.")
