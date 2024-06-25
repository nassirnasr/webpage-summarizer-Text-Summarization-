Sure! Here’s a simple and clear README for your project:

---

# Webpage Summarizer

This project is a web-based application for summarizing text from webpages. It uses Streamlit for the user interface and various natural language processing techniques to extract the most important words and generate a summary from the provided URL.

## Features

- Extracts and summarizes text from any provided webpage URL.
- Displays the most important words in the text.
- Shows a frequency distribution plot of the most important words.
- Provides a clear and concise summary of the webpage content.

## Requirements

- Python 3.6 or higher
- Streamlit
- BeautifulSoup4
- NLTK
- Matplotlib

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/webpage-summarizer.git
    cd webpage-summarizer
    ```

2. **Install the required Python packages:**
    ```sh
    pip install streamlit beautifulsoup4 nltk matplotlib
    ```

3. **Download NLTK data:**
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

## Usage

1. **Save the script to a file (e.g., `web_summarizer.py`):**

    ```python
    import bs4 as bs
    import urllib.request as url
    import re
    import nltk
    import heapq
    import matplotlib.pyplot as plt
    import streamlit as st
    from string import punctuation

    # Ensure necessary NLTK data is downloaded
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
    def generate_summary(sentence_scores, n=7):
        summary_sentences = heapq.nlargest(n, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    # Function to extract most important words
    def most_important_words(word_frequencies, n=30):
        most_important_words = heapq.nlargest(n, word_frequencies, key=word_frequencies.get)
        return most_important_words

    # Main function to run the summarization
    def summarize_webpage(url_address):
        article_text = get_webpage(url_address)
        cleaned_text, formatted_text = text_cleaning(article_text)
        sentences = nltk.sent_tokenize(cleaned_text)
        words = tokenize_and_remove_stopwords(formatted_text)
        word_frequencies = calculate_word_frequencies(words)
        word_frequencies = normalize_frequencies(word_frequencies)
        sentence_scores = score_sentences(sentences, word_frequencies)
        summary = generate_summary(sentence_scores)
        important_words = most_important_words(word_frequencies)
        return summary, important_words, word_frequencies

    # Streamlit UI
    st.title("Webpage Summarizer")

    # Enter URL
    url_address = st.text_input("Enter URL:")

    if st.button("Summarize"):
        if url_address:
            summary, important_words, word_frequencies = summarize_webpage(url_address)
            
            st.subheader("Most Important Words:")
            st.write(", ".join(important_words))
            
            st.subheader("Summary:")
            st.write(summary)
            
            st.subheader("Word Frequency Distribution:")
            # Plot the word frequency distribution
            freq_dist = nltk.FreqDist(word_frequencies)
            plt.figure(figsize=(10, 6))
            freq_dist.plot(30, cumulative=False)
            st.pyplot(plt)
        else:
            st.write("Please enter a valid URL.")
    ```

2. **Run the Streamlit app:**
    ```sh
    streamlit run WebSummarization.py
    ```

3. **Open the provided URL in your browser to interact with the app.**

## Example

1. Enter a valid webpage URL in the input field.
2. Click the "Summarize" button.
3. View the most important words, summary, and word frequency distribution in the output sections.

## License

This project is licensed under the MIT License.
![Screenshot 2024-06-10 111255](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/f03dc381-0daa-42a8-91e1-523021577598)
![Screenshot 2024-05-15 074506](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/6740b862-7132-4936-af84-0217d33ea160)
![Screenshot (10)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/53a88d57-53eb-4104-a467-5ca1327bc593)
![Screenshot (9)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/dc89d7e7-6a08-4ed0-8d41-dce8cae48862)
![Screenshot (8)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/0fdce7c8-6086-4eb1-9434-0b4442c703c1)
![Screenshot (7)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/339eb9a9-78aa-41c8-8457-9d877867eab0)

---

**Here are Screanshots**
