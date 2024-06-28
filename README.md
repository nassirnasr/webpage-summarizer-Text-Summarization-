
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
    git clone https://github.com/nassirnasr/webpage-summarizer-Text-Summarization-.git
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

1. **Save the script to a file (e.g., `Websummarization.py`):**

  

2. **Run the Streamlit app:**
    ```sh
    streamlit run WebSummarization.py
    ```
    or
    ```sh
    streamlit run app.py
    ```

4. **Open the provided URL in your browser to interact with the app.**

## Example

1. Enter a valid webpage URL in the input field.
2. Click the "Summarize" button.
3. View the most important words, summary, and word frequency distribution in the output sections.

## License

This project is licensed under the MIT License.

---

#Here are Screanshots
---
**Run the in VsCode**
---
![Screenshot (7)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/b2906e59-95e2-41be-959d-8b536b832ba0)
---

**Navigate to Browser**
---
![Screenshot (8)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/51b366ef-5d60-411e-b9f8-1a1e6a4aea96)
---
**Paste url from the page you want to summarize**
---
![Screenshot (9)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/21334f0c-d45f-4def-ba64-862827880be4)

---
![Screenshot (10)](https://github.com/nassirnasr/WebPageSummarization_Text_Summarization_With_UI/assets/135421756/8ed880c5-006d-4e5e-8263-31863994b6e7)
---

---


