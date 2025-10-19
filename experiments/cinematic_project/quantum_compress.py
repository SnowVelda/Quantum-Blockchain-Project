from qiskit import QuantumCircuit, execute, Aer
from qiskit.quantum_info import Statevector

def quantum_compress(data):
    # Create a quantum circuit
    qc = QuantumCircuit(len(data))

    # Encode the data into the quantum circuit
    for i, bit in enumerate(data):
        if bit == 1:
            qc.x(i)

    # Apply a Hadamard gate to each qubit
    qc.h(range(len(data)))

    # Measure the qubits
    qc.measure_all()

    # Run the circuit on a simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()

    # Get the compressed data
    compressed_data = result.get_counts()

    return compressed_data

# Example usage
data = [1, 0, 1, 0, 1, 0, 1, 0]
compressed_data = quantum_compress(data)
print(compressed_data)
