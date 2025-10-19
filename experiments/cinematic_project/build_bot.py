import os
import subprocess

# Define the build bot function
def build_bot():
    # Run the C# code to build the blockchain
    subprocess.run(["dotnet", "run", "QuantumBlockchain.csproj"])

    # Run the Qiskit code to compress and encrypt data
    subprocess.run(["python", "quantum_compress.py"])
    subprocess.run(["python", "quantum_encrypt.py"])

    # Run the game code
    subprocess.run(["dotnet", "run", "QuantumGame.csproj"])

# Define the main function
def main():
    build_bot()

if __name__ == "__main__":
    main()
