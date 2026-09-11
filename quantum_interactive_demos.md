# Quantumizers Meetup 3: Interactive QASM Demos

This guide provides copy-pasteable **OpenQASM 2.0** code blocks for each of the 5 algorithms in the presentation. These circuits are designed to run instantly on any standard simulator or cloud QPU (e.g., IBM Quantum Composer, Classiq, or local Qiskit setups).

---

## Demo 1: QAOA (Optimization Solver - Vehicle Routing)

*This circuit represents a simplified 2-location route optimization decision. Qubit 0 represents Route A; Qubit 1 represents Route B. We use gates to apply a "traffic penalty" if both routes are chosen simultaneously.*

### OpenQASM 2.0 Code:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Step 1: Initialize superposition (evaluate all combinations)
h q[0];
h q[1];

// Step 2: Apply cost layer (rotations based on route distance)
rz(pi/4) q[0];
rz(pi/4) q[1];

// Step 3: Apply constraint layer (traffic penalty if both are chosen)
cx q[0], q[1];
rz(pi/2) q[1];
cx q[0], q[1];

// Step 4: Mixer layer (allows state exploration)
h q[0];
h q[1];

// Step 5: Measure output
measure q -> c;
```

### Explanation:

* **The Mathematics Layer:** Qubits act as binary decisions (on/off). The `rz` rotations represent the cost (miles traveled). The CNOT-RZ-CNOT sequence acts as a mathematical logic constraint: it adds a negative phase penalty only if both qubits are in the `1` state (meaning the trucks collide or double-book roads).
* **The Result Layer:** When you run 1024 shots, you will see a non-uniform histogram. Certain states (e.g., `01` or `10`) will have much higher probability peaks than the double-booked `11` state.
* **How We Use the Results:** We read the binary state with the highest probability. If `10` is the tallest bar, it means selecting Route A (`1`) and skipping Route B (`0`) is the mathematically optimal routing decision.

---

## Demo 2: VQE (Simulation Solver - Molecular Energy Minimization)

*This circuit acts as a variational trial state (ansatz) for a Hydrogen molecule ($H_2$). It prepares a parameterized superposition state to find the coordinates of minimum chemical energy.*

### OpenQASM 2.0 Code:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Step 1: Initialize reference state (Hartree-Fock state)
x q[0];

// Step 2: Parametric rotation (simulating electron orbital bond angle)
ry(pi/3) q[1];

// Step 3: Entangle orbitals
cx q[1], q[0];

// Step 4: Measure energy properties
measure q -> c;
```

### Explanation:

* **The Mathematics Layer:** We map molecular orbitals to qubits (Qubit 0 = Orbital 1, Qubit 1 = Orbital 2). The `ry(pi/3)` gate represents a trial parameter (the distance between hydrogen atoms). The CNOT gate models electron-electron interaction (entanglement).
* **The Result Layer:** Running this returns a specific probability distribution of electron configurations (e.g., `01` and `10` states). The energy is calculated by measuring this output and summing up the Hamiltonian values.
* **How We Use the Results:** A classical optimizer reads the energy result, alters the rotation angle slightly (e.g., changing `pi/3` to `pi/4`), and runs the circuit again. This loop runs until the energy plots stop dropping, identifying the exact physical bond length of the molecule.

---

## Demo 3: Grover (Search Solver - Unsorted Database Search)

*This circuit searches a database of 4 items (`00`, `01`, `10`, `11`) and instantly isolates the marked target item `11`.*

### OpenQASM 2.0 Code:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Step 1: Initialize database search space
h q[0];
h q[1];

// Step 2: Oracle (highlight/tag the target state '11')
cz q[0], q[1];

// Step 3: Diffusion Operator (amplify the highlighted target)
h q[0];
h q[1];
x q[0];
x q[1];
cz q[0], q[1];
x q[0];
x q[1];
h q[0];
h q[1];

// Step 4: Measure the database index
measure q -> c;
```

### Explanation:

* **The Mathematics Layer:** We represent 4 database folders as index combinations of 2 qubits. The Oracle gate (`cz`) is a mathematical marker that flips the sign (phase) of only the target state `11` from positive to negative. The diffusion steps act as an amplifier, mirroring all states around the average.
* **The Result Layer:** When measured, the histogram will show a single tall bar at the `11` state with **100% probability**, while all other states (`00`, `01`, `10`) drop to 0%.
* **How We Use the Results:** The measured output binary string `11` corresponds to the index address of the target file in the database, allowing us to find it in 1 step instead of checking all 4 folders.

---

## Demo 4: QRNG (Security & Entropy - Unhackable Cryptography)

*This circuit utilizes 3 qubits to generate a truly random 3-bit binary security key (0 to 7) using physical quantum coin-flips.*

### OpenQASM 2.0 Code:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

// Step 1: Spin 3 coins simultaneously (superposition)
h q[0];
h q[1];
h q[2];

// Step 2: Measure to freeze states and generate entropy
measure q -> c;
```

### Explanation:

* **The Mathematics Layer:** We place 3 independent qubits into a perfect 50/50 superposition state using Hadamard (`h`) gates. There are no classical parameters or mathematical seeds.
* **The Result Layer:** Every run yields a random 3-bit binary string (e.g., `101`, `010`, `111`). Across 1024 shots, you will see an absolutely flat, uniform histogram where all 8 possibilities (`000` to `111`) have an equal ~12.5% chance.
* **How We Use the Results:** We read the raw output bitstring to build unhackable encryption keys. Because the value collapses based on physical atomic fluctuations, a hacker cannot predict or reverse-engineer the key using equations.

---

## Demo 5: QML (Pattern Classification - Fraud Detection)

*This circuit represents a Quantum Kernel classifier. It maps two features of a financial transaction (e.g., transaction amount and time of day) into a high-dimensional quantum state.*

### OpenQASM 2.0 Code:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Step 1: Initialize features space
h q[0];
h q[1];

// Step 2: Feature Map (Encode transaction amount and time as rotations)
rz(0.5) q[0]; // Feature 1: Amount
rz(1.2) q[1]; // Feature 2: Time

// Step 3: Model complex interactions (correlation boundary)
cx q[0], q[1];

// Step 4: Measure state overlap
measure q -> c;
```

### Explanation:

* **The Mathematics Layer:** Qubit rotations represent feature coordinates (amount and time). The CNOT gate projects these coordinates into a higher dimension (Hilbert Space) to find complex correlations that look tangled on a flat classical plane.
* **The Result Layer:** The measurement gives the overlap probability of the data points. Points with similar probabilities belong to the same cluster (e.g. legitimate transactions vs. fraud anomalies).
* **How We Use the Results:** A classical machine learning model reads these quantum overlap scores (kernels) and uses them to draw a clean classification boundary to isolate fraud.
