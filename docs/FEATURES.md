# Project Features

This document outlines the implemented and planned features of the Quantum Blockchain Project.

## Implemented Features

### Core Blockchain (`src/main_blockchain.py`)
- **Quantum-Resistant Transactions**: Uses Dilithium2 post-quantum cryptography to sign and verify transactions, ensuring security against future quantum attacks.
- **Proof-of-Work (PoW)**: Implements a simple nonce-based PoW algorithm for mining new blocks.
- **Standard Blockchain Structure**: Includes standard concepts like Blocks, Transactions, Timestamps, and Hash chains.
- **Mining Rewards**: A system to reward miners for successfully creating new blocks.

### Quantum Miner (`src/quantum_miner.py`)
- **Experimental Quantum Mining**: Utilizes Grover's search algorithm via Qiskit to find valid nonces, exploring a quantum approach to mining.
- **IBM Quantum Integration**: Connects to the Qiskit Runtime Service to run mining jobs on real IBM Quantum hardware.
- **Local Simulator Fallback**: Defaults to a local simulator if real quantum hardware is unavailable.

### Sentient AI Hub (`src/quantum_sentient_ai.py`)
- **Multi-AI Communication**: An interactive CLI that orchestrates communication between different AI models.
- **Dynamic AI Routing**: Can route user prompts to either Gemini or OpenAI models.
- **Mock/Real API Modes**: Features a `toggle_mock` command to switch between using real API calls and returning mock data for safe, offline testing.

## Planned Features (from Roadmap)

- **Supabase Backend Integration**: Full integration for wallet and transaction management.
- **Testnet Deployment**: Public deployment of the QRL application.
- **Performance & Security Auditing**: Formal process to gather metrics and assess security.
- **Investor Pitch Materials**: Refined executive summary and pitch decks based on testnet data.
