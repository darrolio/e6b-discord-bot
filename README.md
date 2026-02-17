# E6B Discord Calculator Bot

A Discord bot that performs E6B flight computer calculations using Google Gemini AI with precise Python code execution.

## Features

- **Wind Correction Angle (WCA) & Groundspeed** - Calculate WCA and GS based on true course, TAS, wind direction, and wind speed
- **Density Altitude** - Calculate density altitude from pressure altitude and OAT
- **Fuel Burn** - Calculate time en route and fuel needed
- **True Airspeed** - Estimate TAS from IAS and altitude

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then edit `.env` and add your API keys:

- **GEMINI_API_KEY**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **DISCORD_TOKEN**: Get from [Discord Developer Portal](https://discord.com/developers/applications)

### 3. Set Up Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a New Application
3. Go to the "Bot" section and create a bot
4. Copy the bot token and add it to your `.env` file
5. Enable "Message Content Intent" in the Bot settings
6. Go to OAuth2 > URL Generator
7. Select scopes: `bot`
8. Select permissions: `Send Messages`, `Read Messages/View Channels`, `Read Message History`
9. Copy the generated URL and use it to invite the bot to your server

### 4. Run the Bot

**Option 1: Using environment variables directly**
```bash
export GEMINI_API_KEY="your_key_here"
export DISCORD_TOKEN="your_token_here"
python bot.py
```

**Option 2: Using python-dotenv (recommended)**
Install python-dotenv:
```bash
pip install python-dotenv
```

Then modify the top of `bot.py` to add:
```python
from dotenv import load_dotenv
load_dotenv()
```

Then run:
```bash
python bot.py
```

## Usage

### Command: `$calc`

Ask any E6B calculation question after the `$calc` command.

**Examples:**

```
$calc I'm flying a true course of 180 at 110 knots TAS. The wind is from 220 at 15 knots. What is my WCA and groundspeed?

$calc Calculate density altitude with pressure altitude 5000ft and OAT 25°C

$calc How much fuel do I need for a 200nm trip at 130 knots groundspeed if I burn 8 GPH?

$calc What's my TAS if I'm indicating 100 knots at 6000 feet?
```

### Command: `$help_e6b`

Shows help information and example commands.

## How It Works

1. The bot receives a calculation question via the `$calc` command
2. The question is sent to Google Gemini with a system prompt that includes the E6B Python class
3. Gemini uses code execution to run the E6B calculations with precise math
4. The result is returned to the Discord channel

## E6B Calculations Reference

The bot uses the following E6B calculation methods:

- `wind_correction(true_course, true_airspeed, wind_direction, wind_speed)` - Returns WCA and groundspeed
- `density_altitude(pressure_alt, oat)` - Returns density altitude
- `fuel_burn(gph, distance, groundspeed)` - Returns time (minutes) and fuel (gallons)
- `true_airspeed_estimate(ias, altitude)` - Returns estimated TAS

## License

MIT

## Contributing

Feel free to submit issues or pull requests!
