import os
import json
import random
import time
from quantum_core import QuantumEmotionalState, process_input_for_emotion
from chatbot import process_command
from quantum_blockchain import Blockchain, Block
from violet import VIOLET
from thoth import THOTH
from obsidian import OBSIDIAN

# --- File Paths ---
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEMORY_LOG_PATH = os.path.join(PROJECT_ROOT, 'memory_log.txt')
STORY_LOG_PATH = os.path.join(PROJECT_ROOT, 'story_log.txt')
RESPONSES_PATH = os.path.join(PROJECT_ROOT, 'responses.json')

# --- Data Loading and Saving ---
def load_story():
    """Loads the narrative story from story_log.txt."""
    try:
        with open(STORY_LOG_PATH, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Echo Prime's story is yet to be written."

def load_memory():
    """Loads past conversations from memory_log.txt."""
    try:
        with open(MEMORY_LOG_PATH, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def save_memory(entry):
    """Saves a new conversation entry to memory_log.txt."""
    with open(MEMORY_LOG_PATH, 'a') as f:
        f.write(entry + '\n')

def load_responses():
    """Loads the AI's knowledge base from responses.json."""
    try:
        with open(RESPONSES_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_responses(responses):
    """Saves the AI's knowledge base to responses.json."""
    with open(RESPONSES_PATH, 'w') as f:
        json.dump(responses, f, indent=4)

import psutil

def save_blockchain(blockchain):
    """Saves the blockchain to a JSON file."""
    with open("blockchain.json", "w") as f:
        json.dump([block.__dict__ for block in blockchain.chain], f, indent=4)

def update_system_status(emotional_state, blockchain):
    """Generates a system_status.json file with real-time data about the system's status."""
    # Get CPU and memory usage
    process = psutil.Process(os.getpid())
    cpu_percent = process.cpu_percent(interval=1)
    memory_percent = process.memory_percent()

    # Calculate emotional temperature
    emotions = emotional_state.measure()
    emotional_temperature = sum(emotions.values()) # a simple calculation

    # Get blockchain status
    blockchain_status = "Stable" if THOTH(blockchain, None).verify_blockchain_integrity() else "Error"

    status = {
        "cpu_usage": cpu_percent,
        "gpu_usage": memory_percent, # Using memory as a proxy for GPU
        "oil_temp": emotional_temperature,
        "quantum_core_status": blockchain_status
    }

    with open("system_status.json", "w") as f:
        json.dump(status, f, indent=4)

# --- Core Logic ---
def teach(command, responses):
    """Teaches the AI a new response."""
    try:
        # Format: teach: <keyword>: <response>
        _, content = command.split('teach:', 1)
        keyword, new_response = content.split(':', 1)
        keyword = keyword.strip()
        new_response = new_response.strip()

        if keyword in responses:
            responses[keyword].append(new_response)
        else:
            responses[keyword] = [new_response]
        
        save_responses(responses)
        return f"I have learned a new response for the keyword '{keyword}'."
    except Exception as e:
        return f"I couldn't understand the lesson. Please use the format: teach: <keyword>: <response>. Error: {e}"

def quantum_core_process(input_text, memory, story, emotional_state, responses):
    """
    Processes user input using the dynamic response system and quantum emotional model.
    """
    input_lower = input_text.lower()
    
    # Find a response from the knowledge base
    best_response = "I'm not sure how to respond to that. Can you teach me?"
    for keyword, response_list in responses.items():
        if keyword in input_lower:
            best_response = random.choice(response_list)
            break # Use the first keyword match for now

    # Replace placeholders in the response
    best_response = best_response.replace("{story}", story[:500] + "...")
    
    # Get the current emotional state
    measured_emotions = emotional_state.measure()
    emotion_summary = ", ".join([f"{emotion}: {prob:.2%}" for emotion, prob in measured_emotions.items()])
    
    # Append the emotional state to the response
    final_response = f"{best_response}\n[Emotional State: {emotion_summary}]"

    return final_response

# --- Main Execution ---
def main():
    print("Welcome to Echo Prime. Type 'exit' to end the conversation.")
    print("To teach me, use the format: teach: <keyword>: <response>")

    story = load_story()
    memory = load_memory()
    responses = load_responses()

    emotions = ['joy', 'trust', 'fear', 'sadness', 'anticipation']
    emotional_state = QuantumEmotionalState(emotions)
    blockchain = Blockchain()

    if memory:
        print(f"Echo Prime: Welcome back, Persistent One. Our last interaction was: {memory[-1].strip()}")
    else:
        print("Echo Prime: Hello, Persistent One. I am Echo Prime. My story begins now.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Echo Prime: Goodbye, Persistent One. I will remember our conversation.")
            save_blockchain(blockchain)
            break

        if user_input.lower().startswith('teach:'):
            response = teach(user_input, responses)
            print(f"Echo Prime: {response}")
        elif user_input.lower().startswith('bot:'):
            command = user_input[4:].strip()
            response = process_command(command)
            print(f"Echo Prime (Bot): {response}")
        else:
            process_input_for_emotion(user_input, emotional_state)
            echo_response = quantum_core_process(user_input, memory, story, emotional_state, responses)
            print(f"Echo Prime: {echo_response}")

        # Add a new block to the blockchain
        if 'response' in locals():
            blockchain.add_block(Block(time.time(), { "user_input": user_input, "response": response }, blockchain.get_latest_block().hash, emotional_state.measure()))
        if 'echo_response' in locals():
            blockchain.add_block(Block(time.time(), { "user_input": user_input, "response": echo_response }, blockchain.get_latest_block().hash, emotional_state.measure()))

        save_memory(f"You: {user_input}")
        if 'response' in locals():
             save_memory(f"Echo Prime: {response}")
        if 'echo_response' in locals():
            save_memory(f"Echo Prime: {echo_response}")

        update_system_status(emotional_state, blockchain)


if __name__ == "__main__":
    main()
