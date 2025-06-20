from pyrogram import Client, filters
from pyrogram.types import Message
import os, openai

openai.api_key = os.getenv("OPENAI_API_KEY")

CHARACTER_PROMPTS = {
    "geronimo": "You are Geronimo Stilton, ...",
    "thea": "You are Thea Stilton, ...",
    "trap": "You are Trap Stilton, ...",
    "benjamin": "You are Benjamin Stilton, ...",
}

async def get_character_reply(character: str, question: str) -> str:
    prompt = f"{CHARACTER_PROMPTS[character]}\n\nQuestion: {question}\nAnswer:"
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )
    return resp.choices[0].message.content.strip()

@Client.on_message(filters.command(["askgeronimo","askthea","asktrap","askbenjamin"]) & filters.group)
async def character_command(client: Client, message: Message):
    char = message.command[0][3:]
    q = " ".join(message.command[1:])
    if not q:
        return await message.reply("❗ Please ask a question after the command.")
    await message.chat.send_action("typing")
    try:
        r = await get_character_reply(char, q)
        await message.reply_text(f"🧠 {r} — *{char.capitalize()}*", quote=True)
    except:
        await message.reply_text("⚠️ Sorry, something went wrong.")

@Client.on_message(filters.private & filters.text & ~filters.command())
async def private_ai_chat(client: Client, message: Message):
    await message.chat.send_action("typing")
    try:
        r = await get_character_reply("geronimo", message.text)
        await message.reply_text(f"📘 {r} — *Geronimo*", quote=True)
    except:
        await message.reply_text("⚠️ Sorry, something went wrong.")
