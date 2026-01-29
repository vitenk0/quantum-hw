from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector, Pauli
from qiskit.visualization import plot_bloch_multivector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
import numpy as np

theta = np.pi/2

#1. 
qc1 = QuantumCircuit(4)
qc1.h(0)
qc1.x(1)
qc1.y(2)
qc1.z(3)

psi1 = Statevector.from_instruction(qc1)
plot_bloch_multivector(psi1, title="Problem 1")

#2.
qc2 = QuantumCircuit(3)
qc2.rx(theta, 0)
qc2.ry(theta, 1)
qc2.rz(theta, 2)

psi2 = Statevector.from_instruction(qc2)
plot_bloch_multivector(psi2, title="Problem 2 (θ=π/2)")

#3.
circ = []
qc3 = QuantumCircuit(1)
circ.append(("|0⟩", qc3.copy()))

qc3.y(0)
circ.append(("Y|0⟩", qc3.copy()))

qc3.p(theta, 0)
circ.append(("P(π/2)Y|0⟩", qc3.copy()))

qc3.t(0)
circ.append(("TP(π/2)Y|0⟩", qc3.copy()))

qc3.s(0)
circ.append(("STP(π/2)Y|0⟩", qc3.copy()))

fig = plt.figure(figsize=(20, 8))
fig.suptitle("Problem 3", fontsize=16)

for i, (label, c) in enumerate(circ):
    psi = Statevector.from_instruction(c)

    bloch = [
        psi.expectation_value(Pauli("X")),
        psi.expectation_value(Pauli("Y")),
        psi.expectation_value(Pauli("Z")),
    ]

    ax = fig.add_subplot(1, len(circ), i + 1, projection="3d")
    plot_bloch_vector(bloch, ax=ax)
    ax.set_title(label, pad=40)

plt.subplots_adjust(left=0, right=1, top=0.90, bottom=0.05, wspace=0.15)
plt.show()