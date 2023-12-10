# Andrew S. Messecar, 2023

import pennylane as qml                     # Import PennyLane under the alias "qml"
# from pennylane import numpy as pnp        # Import NumPy through PennyLane with the alias "pnp"

# Device = "lightning.qubit"
# Device = "default.qubit"
# Device = "lightning.gpu"
Device = "lightning.kokkos"                 # Specify the quantum computing simulator/device to be used.

dev = qml.device( Device , wires = 2 )      # Instantiate a 2-qubit quantum circuit on the device.


@qml.qnode( dev )                           # Decorate using the instantiated circuit.

def Circuit():                              # Declare a function for applying quantum operations.
    qml.Hadamard( wires = 0 )               # Apply a Hadamard gate to the first of the two qubits.
    qml.CNOT( wires = [ 0 , 1 ] )           # Apply a CNOT gate to entangle the two qubits together.
    return qml.probs()                      # Return the two qubits' computational basis state probabilities.

print( Circuit() )                          # Call the declared function and print the output to the user.

# qml.draw_mpl(Circuit)()                   # If programming in a Jupyter notebook, print a diagram of the simulated circuit.

print( qml.draw(Circuit)() )                # Print a diagram of the simulated circuit to the user.
