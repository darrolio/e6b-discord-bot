import os
import discord
from discord.ext import commands
import google.generativeai as genai

# Load environment variables from .env file (optional but recommended)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, will use system environment variables
    pass

# Load E6B computer code to provide to Gemini
with open('e6b_computer.py', 'r') as f:
    e6b_code = f.read()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable not set")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# System prompt that includes the E6B code
SYSTEM_PROMPT = f"""I have provided a Python class that replicates E6B functions. When requesting flight planning help, please use this script and execute Python code to ensure the math is 100% accurate. Do not estimate the results.

Here is the E6B calculator Python code that you must include in your code execution:

```python
{e6b_code}
```

CRITICAL INSTRUCTIONS:
1. Parse the user's question to extract the necessary parameters
2. In your code execution, ALWAYS include the full E6BComputer class definition above, then instantiate it and use it
3. DO NOT try to import e6b_calculator - the class must be defined in your code block
4. After executing the code, provide ONLY the final answer with units
5. DO NOT show the Python code to the user
6. DO NOT show any error messages or traceback - just recalculate if there's an error
7. Present the answer in a clean, professional aviation format

Available methods:
- wind_correction(true_course, true_airspeed, wind_direction, wind_speed) -> (WCA, GS)
- density_altitude(pressure_alt, oat) -> density_altitude
- fuel_burn(gph, distance, groundspeed) -> (time_minutes, fuel_gallons)
- true_airspeed_estimate(ias, altitude) -> tas

Example response format:
"Based on your parameters:
- Wind Correction Angle (WCA): 5.2° right
- Groundspeed: 98.3 knots"
"""


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready to perform E6B calculations.')


@bot.command(name='calc')
async def calculate(ctx, *, question: str):
    """
    Responds to E6B calculation questions using Gemini.
    Usage: $calc <your aviation calculation question>
    """
    try:
        # Show typing indicator while processing
        async with ctx.typing():
            # Create Gemini model with code execution enabled
            model = genai.GenerativeModel(
                model_name='models/gemini-2.5-flash',
                system_instruction=SYSTEM_PROMPT,
                tools='code_execution'
            )

            # Send the question to Gemini
            response = model.generate_content(question)

            # Extract the response text
            if response.text:
                # Clean up the response - remove code blocks and error messages
                cleaned_response = response.text

                # Remove Python code blocks
                import re
                cleaned_response = re.sub(r'```python.*?```', '', cleaned_response, flags=re.DOTALL)
                cleaned_response = re.sub(r'```.*?```', '', cleaned_response, flags=re.DOTALL)

                # Remove common error patterns
                cleaned_response = re.sub(r'Traceback.*?(?=\n\n|\Z)', '', cleaned_response, flags=re.DOTALL)
                cleaned_response = re.sub(r'ModuleNotFoundError:.*?(?=\n\n|\Z)', '', cleaned_response, flags=re.DOTALL)

                # Clean up extra whitespace
                cleaned_response = re.sub(r'\n{3,}', '\n\n', cleaned_response)
                cleaned_response = cleaned_response.strip()

                if cleaned_response:
                    # Discord has a 2000 character limit per message
                    if len(cleaned_response) > 2000:
                        # Split into chunks if needed
                        chunks = [cleaned_response[i:i+2000] for i in range(0, len(cleaned_response), 2000)]
                        for chunk in chunks:
                            await ctx.send(chunk)
                    else:
                        await ctx.send(cleaned_response)
                else:
                    await ctx.send("I couldn't generate a response. Please try rephrasing your question.")
            else:
                await ctx.send("I couldn't generate a response. Please try rephrasing your question.")

    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        print(f"Error in calculate command: {e}")
        await ctx.send(error_msg)


@bot.command(name='help_e6b')
async def help_e6b(ctx):
    """Provides help information about the E6B calculator bot."""
    help_text = """
**E6B Flight Calculator Bot**

Use `$calc` followed by your aviation calculation question.

**Examples:**
• `$calc I'm flying a true course of 180 at 110 knots TAS. The wind is from 220 at 15 knots. What is my WCA and groundspeed?`
• `$calc Calculate density altitude with pressure altitude 5000ft and OAT 25°C`
• `$calc How much fuel do I need for a 200nm trip at 130 knots groundspeed if I burn 8 GPH?`
• `$calc What's my TAS if I'm indicating 100 knots at 6000 feet?`

**Available Calculations:**
✈️ Wind Correction Angle (WCA) and Groundspeed
✈️ Density Altitude
✈️ Fuel Burn and Time En Route
✈️ True Airspeed Estimate

The bot uses AI with precise Python calculations to ensure accuracy.
    """
    await ctx.send(help_text)


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
