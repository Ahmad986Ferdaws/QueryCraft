# QueryCraft

QueryCraft lets you ask your database questions in plain English. It generates safe SQL, runs it, and returns results.

## Features
- Natural language → SQL
- Query execution with sanitization
- Read-only mode
- FastAPI API

## Setup
1. Add `.env` with your OpenAI key.
2. Install: `pip install -r requirements.txt`
3. Run: `uvicorn app.main:app --reload`
