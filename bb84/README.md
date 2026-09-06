# ⚛️ Quantum Key Distribution (BB84) Security Simulator

A production-grade Python simulation of the **BB84 Quantum Key Distribution** protocol, implementing true 2D linear algebra state vectors, quantum probability measurement collapse, and intercept-resend eavesdropping threat detection.

---

## 🛠️ Architecture & Engineering Design

This project avoids "toy" string models in favor of rigorous mathematical simulation. It is built as a modular Python package adhering to professional software engineering standards:

*   **`alice.py`**: Handles cryptographically secure bit generation (`secrets` module) and maps bits into 2D orthogonal polarization states (Rectilinear $+$ and Diagonal $\times$ bases).
*   **`bob.py`**: Simulates photon reception using quantum probability amplitudes ($P = |\langle \psi | \phi \rangle|^2$), enforcing physical measurement collapse.
*   **`eve.py`**: Implements an active Man-in-the-Middle (MitM) intercept-resend attack model to test network vulnerability.
*   **`main.py`**: Orchestrates transmission, executes the sifting protocol, and calculates the **Quantum Bit Error Rate (QBER)** against industry-standard security thresholds.

---

## 🔬 Mathematical State Vectors

Qubits are modeled in two-dimensional Hilbert space:
*   **Rectilinear ($+$):** $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$
*   **Diagonal ($\times$):** $|+\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $|-\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$

When an eavesdropper ("Eve") measures photons in a mismatched basis, Heisenberg's Uncertainty Principle forces a random collapse, injecting a theoretical **~25% error rate** into the transmission.

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/EthanM-programin/BB84_Sim.git](https://github.com/EthanM-programin/BB84_Sim.git)
   cd BB84_Sim