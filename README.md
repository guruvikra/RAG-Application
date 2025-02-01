# Ask to My PDF

A web app that lets you upload a PDF file and ask questions based on its content.

## Features

- Upload a PDF.
- Ask questions related to the PDF.
- Get answers using OpenAI's language model.

## Requirements

- Python 3.7+
- OpenAI API y
- Streamlit
- PyPDF2
- Langchain
- FAISS
- dotenv

## Installation

1. Clone the repo:
    
    ```bash
    
    git clone https://github.com/your-username/ask-to-my-pdf.git
    cd ask-to-my-pdf
    
    ```
    
2. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
3. Set up the environment variable for your OpenAI API key in a `.env` file:
    
    ```
    
    OPENAI_API_KEY=your-openai-api-key
    ```
    

## Usage

1. Run the app:
    
    ```bash
    
    streamlit run app.py
    
    ```
    
2. Upload a PDF and ask questions. The app will find answers based on the content.

##
