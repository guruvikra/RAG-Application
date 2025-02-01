# to load the env variable
from dotenv import load_dotenv

# to use streamlit for ui
import streamlit as st

# to load the pdf and read
from PyPDF2 import PdfReader

# to split the pdf into required lines
from langchain.text_splitter import CharacterTextSplitter

from langchain.embeddings.openai import OpenAIEmbeddings

# to search the similarity in the pdf file
from langchain.vectorstores import FAISS

# this helps to combine wiht llm
from langchain.chains.question_answering import load_qa_chain

# this is the requred llm
from langchain_community.llms import openai
def main():
    load_dotenv()
    # print(os.environ["OPENAI_API_KEY"])
    st.set_page_config(page_title="askPdf")
    st.header("Ask to my Pdf")

    # pdf uploader
    pdf= st.file_uploader("Upload your pdf", type=['pdf'])

    if pdf is not None:
        #read the pdf file
        reader = PdfReader(pdf)
        text = ""
        for page in reader.pages:
            # this goes page by page and add to text
            text += page.extract_text()

        # this helps to split it with chunk by chunk to search fast
        splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
            )
        chunks = splitter.split_text(text)

        embeddings = OpenAIEmbeddings()

        # this helps to search in the provided pdf with help of the embeddings
        document = FAISS.from_texts(chunks,embeddings)

        question = st.text_input("Ask you questions from the pdf you uploaded")
        if question:
            answer = document.similarity_search(question)
            # st.write(answer)
            

            llm =openai.OpenAI()
            chain =load_qa_chain(llm,chain_type="stuff")
            res = chain.run(input_documents=answer,question=question)

            st.write(res)
        # st.write(chunks)



if __name__ == '__main__':
    main()