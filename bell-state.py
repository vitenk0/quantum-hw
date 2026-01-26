from qiskit import QuantumCircuit
import qiskit
from qiskit.primitives import StatevectorSampler

# Build a Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Run on local sampler simulator
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()

print(result[0].data.meas.get_counts())
print(qiskit.__version__)