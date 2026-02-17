#!/bin/bash

# E6B Discord Bot Startup Script

echo "E6B Discord Calculator Bot"
echo "=========================="
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo "Please create a .env file with your API keys."
    echo ""
    echo "Steps:"
    echo "1. Copy .env.example to .env"
    echo "   cp .env.example .env"
    echo ""
    echo "2. Edit .env and add your keys:"
    echo "   - GEMINI_API_KEY from https://makersuite.google.com/app/apikey"
    echo "   - DISCORD_TOKEN from https://discord.com/developers/applications"
    exit 1
fi

# Check if required packages are installed
if ! python -c "import discord" 2>/dev/null; then
    echo "Installing required packages..."
    pip install -r requirements.txt
fi

# Load environment variables and run bot
echo "Starting E6B Discord Bot..."
echo ""

# Export variables from .env file
export $(grep -v '^#' .env | xargs)

# Run the bot
python bot.py
