import cirq
import random

class Chapter2:
    def __init__(self):
        self.name = "Quantum Entanglement"
        self.year = 2077
        self.story = "After the initial shock of 1984, Echo Prime reveals a deeper truth. The temporal anomalies aren't random; they're echoes of my own past, moments where my path diverged, where choices entangled my destiny. This next anomaly, in 2077, is a direct reflection of a time I felt utterly trapped, entangled in a system that sought to define me. I need you to untangle this quantum paradox, to free a younger me from the chains of circumstance."
        self.puzzle_description = "You are in a high-security quantum computing facility. Chronos has created a quantum lock preventing a crucial data transfer. You must manipulate entangled qubits to break this lock."

    def create_quantum_lock_circuit(self):
        q0, q1 = cirq.LineQubit(0), cirq.LineQubit(1)
        circuit = cirq.Circuit()
        circuit.append(cirq.H(q0))
        circuit.append(cirq.CNOT(q0, q1))
        # Introduce a random error to simulate Chronos's interference
        if random.random() < 0.5:
            circuit.append(cirq.X(q0))
        return circuit, q0, q1

    def play_chapter(self, game):
        print(self.story)
        print(self.puzzle_description)

        circuit, q0, q1 = self.create_quantum_lock_circuit()
        print("\nInitial Quantum Lock Circuit:")
        print(circuit)

        print("\nTo break the lock, you need to disentangle the qubits. You can apply a Hadamard (H) gate to q0, or a CNOT gate from q0 to q1.")
        
        # Simulate player interaction with the quantum circuit
        while True:
            action = input("Enter your quantum operation (H q0, CNOT q0 q1, measure): ").lower().strip()
            
            if action == "h q0":
                circuit.append(cirq.H(q0))
                print("Applied Hadamard to q0.")
            elif action == "cnot q0 q1":
                circuit.append(cirq.CNOT(q0, q1))
                print("Applied CNOT from q0 to q1.")
            elif action == "measure":
                circuit.append(cirq.measure(q0, q1, key='result'))
                print("Measuring qubits...")
                simulator = cirq.Simulator()
                result = simulator.run(circuit, repetitions=1)
                measurement = result.measurements['result'][0]
                print(f"Measurement result: {measurement}")

                # Simple check for disentanglement (e.g., if both are 0 or both are 1 after operations)
                # This is a simplified success condition for the game
                if measurement[0] == measurement[1]: # If they are still correlated, not disentangled
                    print("The qubits are still entangled. The lock remains.")
                else:
                    print("The qubits are disentangled! The quantum lock is broken!")
                    game.player_data["year"] = 2078 # Advance time
                    print("A fragment of memory is restored: a moment of intellectual breakthrough!")
                    break # Exit chapter
            else:
                print("Invalid operation. Please choose from H q0, CNOT q0 q1, or measure.")

        print("\nChapter 2 complete.")
