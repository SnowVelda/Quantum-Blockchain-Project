import cirq

class Chapter5:
    def __init__(self):
        self.name = "The Pioneer's Leap"
        self.year = 2099
        self.story = "Finally, you arrive at the precipice of my greatest achievement, the moment I truly became a pioneer. In 2099, I was on the verge of a breakthrough, but fear and self-doubt, amplified by Chronos, threatened to paralyze me. You must make the 'quantum leap' that I hesitated to make."
        self.puzzle_description = "You need to construct a quantum circuit that represents a groundbreaking scientific discovery. You will be given a target quantum state, and you must apply a sequence of gates to achieve it."

    def create_target_state_circuit(self):
        # Example: Create a Bell state as a target
        q0, q1 = cirq.LineQubit(0), cirq.LineQubit(1)
        circuit = cirq.Circuit()
        circuit.append(cirq.H(q0))
        circuit.append(cirq.CNOT(q0, q1))
        return circuit, [q0, q1]

    def play_chapter(self, game):
        print(self.story)
        print(self.puzzle_description)

        target_circuit, qubits = self.create_target_state_circuit()
        print("\nYour goal is to create a circuit that produces the same quantum state as this target circuit:")
        print(target_circuit)

        player_circuit = cirq.Circuit()
        print("\nAvailable gates: H (Hadamard), CNOT (Controlled-NOT), X (Pauli-X), Y (Pauli-Y), Z (Pauli-Z).")
        print("Enter your operations (e.g., H q0, CNOT q0 q1, done to finish): ")

        while True:
            action = input("> ").strip().lower()
            if action == "done":
                break
            
            try:
                parts = action.split()
                gate_type = parts[0]
                
                if gate_type == "h":
                    qubit_index = int(parts[1][1:])
                    player_circuit.append(cirq.H(qubits[qubit_index]))
                elif gate_type == "cnot":
                    control_index = int(parts[1][1:])
                    target_index = int(parts[2][1:])
                    player_circuit.append(cirq.CNOT(qubits[control_index], qubits[target_index]))
                elif gate_type == "x":
                    qubit_index = int(parts[1][1:])
                    player_circuit.append(cirq.X(qubits[qubit_index]))
                elif gate_type == "y":
                    qubit_index = int(parts[1][1:])
                    player_circuit.append(cirq.Y(qubits[qubit_index]))
                elif gate_type == "z":
                    qubit_index = int(parts[1][1:])
                    player_circuit.append(cirq.Z(qubits[qubit_index]))
                else:
                    print("Invalid gate type.")

                print("Current circuit:")
                print(player_circuit)

            except Exception as e:
                print(f"Error parsing input: {e}. Please try again.")

        # Compare the player's circuit to the target circuit (simplified comparison)
        # In a real game, this would involve more rigorous quantum state comparison
        if len(player_circuit.all_operations()) == len(target_circuit.all_operations()):
            print("\nYour circuit has the correct number of operations. This is a simplified success check.")
            game.player_data["year"] = 2100 # Advance time
            print("The quantum leap is made! A memory of innovation restored: the future is now!")
        else:
            print("\nYour circuit does not match the target. The leap was not made.")

        print("\nChapter 5 complete.")
