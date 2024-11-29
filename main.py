import torch
from transformers import pipeline
import pennylane as qml
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator  # Corrected import for AerSimulator

# Test if libraries are working
print(torch.__version__)
print("Hugging Face Transformers loaded")
print("PennyLane loaded")
print("Qiskit loaded")

# Example quantum circuit with Qiskit and Aer
def create_quantum_circuit():
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Apply Hadamard gate
    qc.measure(0, 0)  # Measure qubit

    # Use AerSimulator to run the quantum circuit
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit)
    result = job.result()

    print("Quantum Circuit Result:", result.get_counts())

# Run the quantum circuit
create_quantum_circuit()
