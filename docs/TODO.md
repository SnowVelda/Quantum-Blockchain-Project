# Project To-Do List

This is a list of action items based on the project roadmap and current status.

## Phase 1: Infrastructure & Backend

- [ ] **1. Initialize Supabase Project:**
    - [ ] Create a new Supabase project if one doesn't exist.
    - [ ] Define the database schema for `wallets` and `transactions`.
- [ ] **2. Develop Wallet Management Code:**
    - [ ] Choose a backend language (e.g., Python, TypeScript).
    - [ ] Write server-side functions for wallet creation, balance queries, and updates.
- [ ] **3. Integrate with Supabase:**
    - [ ] Connect the QRL PoC to the Supabase backend.
    - [ ] Replace any local/mock data handling with live calls to the Supabase API.

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

## Maintenance

- [ ] **Recreate `requirements.txt`**: The original file was lost during the reorganization. It needs to be recreated with all necessary dependencies (e.g., `pqc_dilithium`, `qiskit`, `numpy`, `openai`).
