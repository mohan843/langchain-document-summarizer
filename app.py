import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

def summarize_text(text):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)
    return summary

if __name__ == "__main__":
    sample_text = """
    LangChain is a framework for developing applications powered by language models. 
    It enables applications that are context-aware (connect a language model to sources of context) 
    and reason (rely on a language model to reason about how to respond).
    The main value props of LangChain are:
    1. Components: composable tools and integrations for working with language models.
    2. Off-the-shelf chains: built-in assemblages of components for higher-level tasks.
    """
    print("Summarizing document...")
    print(summarize_text(sample_text))