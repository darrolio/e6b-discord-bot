# E6B Discord Bot - Project Overview

## What This Is

A Discord bot that performs accurate E6B flight computer calculations using Google's Gemini AI with Python code execution. Users can ask aviation calculation questions in Discord, and the bot uses the E6B Python class to provide mathematically precise answers.

## Project Structure

```
e6b/
├── bot.py                  # Main Discord bot application
├── e6b_computer.py         # E6B calculator class with all aviation formulas
├── test_e6b.py            # Test suite for E6B calculations
├── run_bot.sh             # Startup script for the bot
├── requirements.txt        # Python dependencies
├── .env.example           # Template for environment variables
├── .gitignore             # Git ignore file
├── README.md              # Full documentation
├── QUICKSTART.md          # Quick setup guide
└── PROJECT_OVERVIEW.md    # This file
```

## Key Files

### `e6b_computer.py`
Contains the `E6BComputer` class with methods for:
- Wind Correction Angle (WCA) and Groundspeed calculations
- Density Altitude calculations
- Fuel burn and time en route
- True Airspeed estimates

### `bot.py`
The Discord bot that:
1. Loads the E6B Python code
2. Provides it to Gemini with the system prompt you specified
3. Processes `$calc` commands from Discord users
4. Returns accurate calculations using Gemini's code execution

### `test_e6b.py`
Test script to verify all E6B calculations work correctly before running the bot.

## How It Works

1. User types: `$calc I'm flying a true course of 180 at 110 knots TAS. The wind is from 220 at 15 knots. What is my WCA and groundspeed?`

2. Bot receives the question and sends it to Gemini with the system prompt:
   ```
   "I have provided a Python class that replicates E6B functions.
   When requesting flight planning help, please use this script and
   execute Python code to ensure the math is 100% accurate.
   Do not estimate the results."
   ```

3. Gemini uses the E6B Python class to calculate the answer with code execution

4. Bot returns the precise answer to the Discord channel

## Setup Requirements

1. **Python 3.8+**
2. **Discord Bot Token** - from Discord Developer Portal
3. **Gemini API Key** - from Google AI Studio
4. **Python packages**: discord.py, google-generativeai, python-dotenv

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create `.env` file with your keys:
   ```
   GEMINI_API_KEY=your_key_here
   DISCORD_TOKEN=your_token_here
   ```

3. Run the bot:
   ```bash
   python bot.py
   ```

See `QUICKSTART.md` for detailed setup instructions.

## Example Usage

**Wind Correction:**
```
$calc I'm flying a true course of 180 at 110 knots TAS.
The wind is from 220 at 15 knots. What is my WCA and groundspeed?
```

**Density Altitude:**
```
$calc Calculate density altitude with pressure altitude 5000ft and OAT 25°C
```

**Fuel Planning:**
```
$calc How much fuel do I need for a 200nm trip at 130 knots
groundspeed if I burn 8 GPH?
```

**True Airspeed:**
```
$calc What's my TAS if I'm indicating 100 knots at 6000 feet?
```

## Available Commands

- `$calc <question>` - Ask any E6B calculation question
- `$help_e6b` - Show help and examples

## Technical Details

- **Discord API**: Using discord.py library
- **AI Model**: Google Gemini 2.0 Flash Experimental
- **Code Execution**: Gemini's built-in code execution for precise calculations
- **Calculation Methods**: Based on standard E6B flight computer formulas

## E6B Calculation Methods

All calculations use the standard E6B flight computer formulas:

1. **Wind Correction Angle (WCA)**
   - Formula: `WCA = arcsin((wind_speed × sin(wind_direction - true_course)) / true_airspeed)`
   - Returns: WCA in degrees and Groundspeed in knots

2. **Density Altitude**
   - Formula: `DA = PA + (120 × (OAT - ISA_temp))`
   - Returns: Density altitude in feet

3. **Fuel Burn**
   - Calculates time en route and fuel required
   - Returns: Time in minutes and fuel in gallons

4. **True Airspeed**
   - Rule of thumb: TAS increases 2% per 1000ft altitude
   - Returns: TAS in knots

## Testing

Run the test suite to verify calculations:

```bash
python test_e6b.py
```

This will run example calculations for all E6B methods.

## Notes

- The bot uses Gemini's code execution feature to ensure 100% accurate math
- All calculations are based on standard aviation formulas
- The E6B class can be easily extended with more aviation calculations
- Discord has a 2000 character message limit (bot handles splitting long responses)

## Future Enhancements

Potential additions:
- True Heading calculations
- Magnetic variation corrections
- Crosswind component calculations
- Climb/descent planning
- Weight and balance
- Conversions (nautical miles, statute miles, kilometers, etc.)

## Support

For issues or questions about the bot, refer to:
- `README.md` - Full documentation
- `QUICKSTART.md` - Setup guide
- E6B Wikipedia: https://en.wikipedia.org/wiki/E6B

Happy Flying! ✈️
