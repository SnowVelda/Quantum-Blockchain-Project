#!/usr/bin/env python3
import os
import sys
import subprocess

try:
    import qiskit
    import qiskit_ibm_runtime
    import numpy
except ImportError:
    print("Installing required Python packages: qiskit, qiskit-ibm-runtime, numpy...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "qiskit", "qiskit-ibm-runtime", "numpy"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages: {e}")
        sys.exit(1)

import hashlib
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.circuit.library import GroverOperator
from qiskit_algorithms import Grover
from qiskit.primitives import Sampler as LocalSampler  # Fallback

# Args: target_hex (full target), start_nonce (int), space_size (int)
if len(sys.argv) != 4:
    print("Usage: python3 quantum_miner.py <target_hex> <start_nonce> <space_size>")
    sys.exit(1)

target_hex = sys.argv[1]
start_nonce = int(sys.argv[2])
space_size = int(sys.argv[3])
n_qubits = int(np.log2(space_size))
if n_qubits > 8:  # Limit for real IBM free tier
    n_qubits = 8
    space_size = 2**n_qubits

token = os.getenv('IBMQ_TOKEN')
if not token:
    print("NOT_FOUND: No IBMQ_TOKEN")
    sys.exit(1)

# Real IBM or fallback to local sim (but prefer real)
service = QiskitRuntimeService(channel="ibm_quantum", token=token)
try:
    backend = service.least_busy(operational=True, simulator=False, min_num_qubits=n_qubits)
    sampler = Sampler(backend=backend)
    print(f"Using real IBM: {backend.name}")
except:
    print("IBM busy; using local sim for now.")
    sampler = LocalSampler()

# Grover Setup: Search for nonce where hash(block_data + nonce) < target
# Note: For demo, we approximate oracle with a simple function. In prod, compile to circuit.
def is_valid_nonce(nonce):
    # Simulate full prepareData hash (simplified: data + nonce str)
    data_str = f"quantum_block_data_{nonce}_{target_hex}"  # Mimic Go's prepareData
    hash_obj = hashlib.sha256(data_str.encode())
    hash_hex = hash_obj.hexdigest()
    target_int = int(target_hex, 16)
    hash_int = int(hash_hex, 16)
    return hash_int < target_int  # Real validation

# Custom oracle circuit (marks valid states)
qc_oracle = QuantumCircuit(n_qubits)
# For simplicity, mark states where nonce_index leads to valid (expand for full Grover)
for i in range(space_size):
    if is_valid_nonce(start_nonce + i):
        # Binary state for i
        state = format(i, f'0{n_qubits}b')
        # CZ or phase flip on this state (basic marking)
        indices = [int(bit) for bit in state[::-1]]  # Qiskit qubit order
        if len(indices) == n_qubits:
            qc_oracle.x(range(n_qubits))  # Placeholder flip; real: use multi-controlled Z
            qc_oracle.cz(0, 1)  # Demo gate; customize per state

# Grover operator
grover = Grover(oracle=qc_oracle, iterations=1)  # 1 iter for small space

# Full circuit
qc = QuantumCircuit(n_qubits)
qc.h(range(n_qubits))  # Superposition
qc.compose(grover, inplace=True)
qc.measure_all()

# Run
job = sampler.run(qc, shots=1024)
result = job.result()
counts = result.quasi_dists[0].binary_probabilities() if hasattr(result, 'quasi_dists') else result.quasi_dists

# Find best candidate
max_prob = 0
best_index = -1
for state, prob in counts.items():
    if prob > max_prob:
        max_prob = prob
        best_index = int(state[::-1], 2)  # Reverse for little-endian

if best_index != -1:
    candidate_nonce = start_nonce + best_index
    if is_valid_nonce(candidate_nonce):
        print(f"FOUND: {candidate_nonce}")
        if hasattr(job, 'job_id'):
            print(f"Real IBM Job ID: {job.job_id()}")
    else:
        print("NOT_FOUND")
else:
    print("NOT_FOUND")