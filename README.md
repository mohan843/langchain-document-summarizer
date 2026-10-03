# LangChain Document Summarizer (RAG)

This project is part of a 5-day GitHub project sprint. It demonstrates a simple Retrieval-Augmented Generation (RAG) style summarization using LangChain.

## Features
- Loads text documents.
- Splits text into chunks.
- Uses a summarization chain to generate a concise summary.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the summarizer:
   ```bash
   python app.py
   ```