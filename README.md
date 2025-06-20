# Geronimo Stilton AI Bot

NFTelegram bot using Pyrogram & OpenAI.

## Setup
1. Copy `.env.example` to `.env`
2. Fill in your BOT_TOKEN, API_ID, API_HASH, OPENAI_API_KEY
3. Install dependencies:
   `pip install pyrogram openai python-dotenv tgcrypto`
4. Run locally:
   `python main.py`

## Deploy on Render
Use Python web service:
- Build command: `pip install -r requirements.txt`
- Start command: `python main.py`
- Set env vars accordingly
