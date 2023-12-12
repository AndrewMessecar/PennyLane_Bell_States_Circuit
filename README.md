Andrew S. Messecar, 2023

This Python 3 script was developed as a simple introductory exercise during the 28 November 2023 "Using PennyLane on Pawsey's Setonix supercomputer" webinar. In addition to the Python3 open-source programming language, it requires the "pennylane", "pennylane-lightning", and "pennylane-lightning[kokkos]" libraries, all of which are freely available to be installed via pip3.

The program serves as a "Hello World"-esque quantum computing 101 exercise in the PennyLane programming environment. The script initializes a 2-qubit circuit on a specified quantum computing device or simulator. More information about available devices is provided at https://pennylane.ai/plugins/

A quantum node or "QNode" is then created by decorating using the initialized 2-qubit circuit.

Following this, a user-defined function is declared which applies a Hadamard gate to the first of the two qubits in the circuit; this places the first qubit in a state of superposition. The function proceeds to entangle the two qubits together via a Controlled NOT (CNOT) gate before returning the probability values of both qubits occupying each of the computational basis states to the user in lexicographic order.

The program concludes by calling this user-defined function, printing the returned probability values to the user, and then printing a diagram of the simulated circuit to the user.

Additional capabilities of the PennyLane environment that were discussed in the webinar but are non-essential to the basic functionality of the script have been commented out. These include: importing NumPy through PennyLane using a separate alias, changing between plugins to run the simulated circuit on different quantum computing simulators or devices, and a separate function for drawing the simulated quantum computing circuit when programming with PennyLane in Jupyter notebooks.
