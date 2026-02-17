# Quick Start Guide

Get your E6B Discord bot running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
pip install python-dotenv
```

## Step 2: Get Your API Keys

### Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key

### Discord Bot Token
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Give it a name (e.g., "E6B Calculator")
4. Go to the "Bot" section in the left sidebar
5. Click "Add Bot"
6. Under "Privileged Gateway Intents", enable "Message Content Intent"
7. Click "Reset Token" and copy the token

## Step 3: Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and paste your keys:

```
GEMINI_API_KEY=your_gemini_api_key_here
DISCORD_TOKEN=your_discord_token_here
```

## Step 4: Invite Bot to Your Server

1. In Discord Developer Portal, go to OAuth2 > URL Generator
2. Under "Scopes", check `bot`
3. Under "Bot Permissions", check:
   - Read Messages/View Channels
   - Send Messages
   - Read Message History
4. Copy the generated URL at the bottom
5. Paste it in your browser and select your server

## Step 5: Update bot.py

Add this import at the top of `bot.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

So the top of your file looks like:

```python
import os
import discord
from discord.ext import commands
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load E6B computer code to provide to Gemini
with open('e6b_computer.py', 'r') as f:
    e6b_code = f.read()
...
```

## Step 6: Run the Bot

```bash
python bot.py
```

Or use the startup script:

```bash
./run_bot.sh
```

You should see:
```
E6BBot#1234 has connected to Discord!
Bot is ready to perform E6B calculations.
```

## Step 7: Test It!

Go to your Discord server and type:

```
$calc I'm flying a true course of 180 at 110 knots TAS. The wind is from 220 at 15 knots. What is my WCA and groundspeed?
```

The bot should respond with the calculated Wind Correction Angle and Groundspeed!

## Troubleshooting

**Bot doesn't respond:**
- Make sure "Message Content Intent" is enabled in Discord Developer Portal
- Check that the bot has permission to read and send messages in the channel

**Import errors:**
- Make sure all dependencies are installed: `pip install -r requirements.txt python-dotenv`

**API key errors:**
- Verify your keys are correctly set in the `.env` file
- Make sure there are no extra spaces or quotes around the keys

## Commands

- `$calc <question>` - Ask any E6B calculation question
- `$help_e6b` - Show help and examples

## Examples

```
$calc Calculate density altitude with pressure altitude 5000ft and OAT 25°C

$calc How much fuel do I need for a 200nm trip at 130 knots groundspeed if I burn 8 GPH?

$calc What's my TAS if I'm indicating 100 knots at 6000 feet?
```

Enjoy your E6B calculator bot! ✈️
