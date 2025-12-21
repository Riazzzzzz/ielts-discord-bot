import discord
import asyncio
import os
from discord.ext import commands

from part1_questions import get_10_part1_questions
from part23_questions import get_part2_and_part3

# ---------------- BOT SETUP ----------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- BOT EVENTS ----------------

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")

# ---------------- COMMAND ----------------

@bot.command()
async def ielts(ctx, part: str):
    part = part.lower()

    # -------- PART 1 --------
    if part == "part1":
        questions = get_10_part1_questions()
        message = "🎤 **IELTS Speaking Part 1 – Practice Set**\n\n"

        for i, q in enumerate(questions, start=1):
            message += f"{i}. {q}\n"

        await ctx.send(message)

    # -------- PART 2 & 3 --------
    elif part == "part2":
        part2, part3_questions = get_part2_and_part3()

        # Part 2 cue card
        await ctx.send(f"🎤 **IELTS Speaking Part 2 (Cue Card)**\n\n{part2}")

        # Preparation time
        await ctx.send("⏱️ **Preparation Time: 1 minute** — start preparing now.")
        await asyncio.sleep(60)

        # Speaking time
        await ctx.send("🗣️ **Speaking Time: 2 minutes** — start speaking now.")
        await asyncio.sleep(120)

        # Part 3 follow-up questions
        message = "🎤 **IELTS Speaking Part 3 (Follow-up Questions)**\n\n"
        for i, q in enumerate(part3_questions, start=1):
            message += f"{i}. {q}\n"

        await ctx.send(message)

    # -------- INVALID INPUT --------
    else:
        await ctx.send("❌ Use: `!ielts part1` or `!ielts part2`")

# ---------------- RUN BOT ----------------

bot.run(os.getenv("TOKEN"))
