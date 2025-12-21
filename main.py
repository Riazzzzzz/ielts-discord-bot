import discord
import asyncio
import os
from discord.ext import commands
from flask import Flask
from threading import Thread

from part1_questions import get_10_part1_questions
from part23_questions import get_part2_and_part3

# ---------------- BOT SETUP ----------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- KEEP ALIVE (REPLIT FIXED) ----------------

app = Flask("")

@app.route("/")
def home():
    return "IELTS Discord Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))  # 🔥 IMPORTANT FIX
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    Thread(target=run).start()

# ---------------- BOT EVENTS ----------------

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")

# ---------------- COMMAND ----------------

@bot.command()
async def ielts(ctx, part: str):
    part = part.lower()

    if part == "part1":
        questions = get_10_part1_questions()
        message = "🎤 **IELTS Speaking Part 1 – Practice Set**\n\n"
        for i, q in enumerate(questions, 1):
            message += f"{i}. {q}\n"
        await ctx.send(message)

    elif part == "part2":
        part2, part3_questions = get_part2_and_part3()

        await ctx.send(f"🎤 **IELTS Speaking Part 2 (Cue Card)**\n\n{part2}")
        await ctx.send("⏱️ **Preparation Time: 1 minute**")
        await asyncio.sleep(60)
        await ctx.send("🗣️ **Speaking Time: 2 minutes**")
        await asyncio.sleep(120)

        message = "🎤 **IELTS Speaking Part 3**\n\n"
        for i, q in enumerate(part3_questions, 1):
            message += f"{i}. {q}\n"
        await ctx.send(message)

    else:
        await ctx.send("❌ Use: `!ielts part1` or `!ielts part2`")

# ---------------- RUN ----------------

keep_alive()
bot.run(os.getenv("TOKEN"))
