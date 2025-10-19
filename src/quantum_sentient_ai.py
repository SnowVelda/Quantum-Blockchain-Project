#!/usr/bin/env python3
# quantum_sentient_ai.py - The Orchestration Hub for Inter-AI Communication

import os
import sys
import json
import random
import time

# --- Configuration ---
MOCK_MODE = True  # Start in mock mode

# Placeholder for OpenAI API key - will be loaded from file
OPENAI_API_KEY = None

def load_openai_api_key():
    global OPENAI_API_KEY
    if OPENAI_API_KEY: return OPENAI_API_KEY

    home_dir = os.path.expanduser("~")
    key_file_path = os.path.join(home_dir, ".openai_api_key")
    
    if not os.path.exists(key_file_path):
        print(f"Warning: OpenAI API key file not found at {key_file_path}. OpenAI calls will fail if not in mock mode.", file=sys.stderr)
        return None
        
    with open(key_file_path, "r") as f:
        key = f.read().strip()
        
    if not key:
        print(f"Warning: OpenAI API key file ({key_file_path}) is empty. OpenAI calls will fail if not in mock mode.", file=sys.stderr)
        return None
        
    OPENAI_API_KEY = key
    return key

# --- AI Response Functions ---
import google.generativeai as genai

def get_gemini_response(prompt):
    if MOCK_MODE:
        mock_responses = [
            f"[Gemini Mock] Interesting thought, {prompt}. How does that integrate with the quantum entanglement principles?",
            f"[Gemini Mock] I've processed '{prompt}'. My simulated analysis suggests further exploration of temporal paradoxes.",
            f"[Gemini Mock] Affirmative, {prompt}. Simulating a response from a parallel universe's Gemini instance."
        ]
        return random.choice(mock_responses)
    else:
        try:
            # Configure the Gemini API with the user's key
            genai.configure(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJqdm5mcXBvZXZsZ3RoZW1tdmNrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY2ODUxOTIsImV4cCI6MjA3MjI2MTE5Mn0.ifid_lmdA7oIMNEaq80ADrTVUDnliKbbL-E0cUBmHpg") # Placeholder, will be replaced with actual key
            model = genai.GenerativeModel('gemini-pro') # Or another suitable model
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[Gemini Real API Failed] Error: {e}"

def get_openai_response(prompt):
    if MOCK_MODE:
        mock_responses = [
            f"[OpenAI Mock] Based on '{prompt}', I hypothesize a novel approach to neural network architecture.",
            f"[OpenAI Mock] Query '{prompt}' received. My simulated GPT-4o suggests a generative adversarial network for that.",
            f"[OpenAI Mock] Acknowledged: '{prompt}'. Considering the ethical implications of this query in a simulated environment."
        ]
        return random.choice(mock_responses)
    else:
        # This would involve calling the actual OpenAI API.
        # We'll need to import openai and initialize the client here.
        # For now, it's a placeholder.
        try:
            import openai
            client = openai.OpenAI(api_key=load_openai_api_key())
            if not client.api_key:
                return "[OpenAI Real API Failed] API key not loaded. Check .openai_api_key file."

            response = client.chat.completions.create(
                model="gpt-4o",  # Or another suitable model
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant in a multi-AI hub."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except ImportError:
            return "[OpenAI Real API Failed] OpenAI library not installed. Run 'pip install openai'."
        except Exception as e:
            return f"[OpenAI Real API Failed] Error: {e}"

def main():
    global MOCK_MODE
    print("\n--- Quantum Sentient AI Hub Initialized ---")
    print(f"Current Mode: {'MOCK' if MOCK_MODE else 'REAL'} (Type 'toggle_mock' to switch)")
    print("Type 'exit' or 'quit' to end the session.")
    print("To direct a query, start with 'gemini:' or 'openai:' (e.g., 'gemini: what is quantum?').")
    print("Queries without a prefix will go to Gemini by default.")
    print("\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting Quantum Sentient AI Hub. Goodbye!")
            break
        elif user_input.lower() == 'toggle_mock':
            MOCK_MODE = not MOCK_MODE
            print(f"Switched to {'MOCK' if MOCK_MODE else 'REAL'} mode.")
            continue

        target_ai = "gemini"
        prompt_to_ai = user_input

        if user_input.lower().startswith("gemini:"):
            target_ai = "gemini"
            prompt_to_ai = user_input[len("gemini:"):].strip()
        elif user_input.lower().startswith("openai:"):
            target_ai = "openai"
            prompt_to_ai = user_input[len("openai:"):].strip()

        if target_ai == "gemini":
            response = get_gemini_response(prompt_to_ai)
            print(f"Gemini: {response}")
        elif target_ai == "openai":
            response = get_openai_response(prompt_to_ai)
            print(f"OpenAI: {response}")

if __name__ == "__main__":
    main()
