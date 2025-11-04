# Project To-Do List

This is a list of action items based on the project roadmap and current status.

## Development Environment Setup

- [ ] **1. Integrate Google Gemini with Visual Studio Code:**
    - [ ] Install necessary extensions and configure VS Code for Gemini integration.

## Phase 1: Infrastructure & Backend

- [x] **1. Initialize Database (SQLite):**
    - [x] Set up SQLite database for `wallets` and `transactions`.
- [x] **2. Develop Wallet Management Code:**
    - [x] Choose a backend language (Python).
    - [x] Write server-side functions for wallet creation, balance queries, and updates (using SQLite).
- [x] **3. Integrate Database:**
    - [x] Connect the QRL PoC to the SQLite backend.
    - [x] Replace any local/mock data handling with live calls to the SQLite database.

## Phase 2: Testnet & Metrics

- [ ] **4. Deploy to a Testnet:**
    - [ ] Deploy the integrated QRL application to a public-facing environment.
- [ ] **5. Performance & Security Audit:**
    - [ ] Run a series of transactions to gather performance metrics (e.g., transactions per second, confirmation time).
    - [ ] Document the results to be used in the pitch deck.

## Phase 3: Investor Outreach

- [ ] **6. Finalize Executive Summary:**
    - [ ] Update the draft with the real-world metrics from the testnet.
    - [ ] Add details on the team and any achievements.
- [ ] **7. Tailor Pitches:**
    - [ ] Create specific versions of the pitch for our target investors (GV, Glasswing, etc.).

## Phase 4: Network Goals

- [ ] **8. Setup Testnet Environment:**
    - [ ] Configure and launch a stable, public-facing testnet.
- [ ] **9. Plan Mainnet Deployment:**
    - [ ] Outline the technical and operational steps required for a mainnet launch.

## Maintenance

- [x] **Recreate `requirements.txt`**: The original file was lost during the reorganization. It needs to be recreated with all necessary dependencies (e.g., `pqc_dilithium`, `qiskit`, `numpy`, `openai`).