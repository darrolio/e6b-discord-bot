#!/usr/bin/env python3
"""
Simple script to check available Gemini models
"""

import os

GEMINI_API_KEY = 'AIzaSyCArX7bWiu4D-MoDmj-697j6XghRU0luUM'

if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY environment variable not set")
    print("Make sure your .env file exists and contains GEMINI_API_KEY")
    exit(1)

print(f"API Key found (first 10 chars): {GEMINI_API_KEY[:10]}...")
print("\nTrying to import google.generativeai...")

try:
    import google.generativeai as genai
    print("✓ google.generativeai imported successfully")
except ImportError as e:
    print(f"✗ Failed to import: {e}")
    print("\nRun: pip install google-generativeai")
    exit(1)

print("\nConfiguring Gemini API...")
genai.configure(api_key=GEMINI_API_KEY)

print("\nFetching available models...\n")
print("=" * 70)

try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"\n✓ Model: {model.name}")
            print(f"  Display Name: {model.display_name}")
            print(f"  Methods: {', '.join(model.supported_generation_methods)}")
except Exception as e:
    print(f"\n✗ Error listing models: {e}")
    print("\nThis might mean:")
    print("1. Your API key is invalid")
    print("2. You need to enable the Gemini API in Google Cloud Console")
    print("3. There's a network issue")
    exit(1)

print("\n" + "=" * 70)
print("\nRecommended models for code execution:")
print("  - gemini-1.5-flash")
print("  - gemini-1.5-pro")
