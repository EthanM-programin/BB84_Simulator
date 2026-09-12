import time
import math
import random
import sys
import numpy as np

# ANSI Color Codes for SOC Dashboard
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class EntanglementNode:
    """Simulates a central quantum network node distributing Bell pairs using 4D Tensor Math."""
    def __init__(self):
        # 1. Define fundamental 2D basis vector |0> and |1>
        self.ket_0 = np.array([1, 0])
        self.ket_1 = np.array([0, 1])

        # 2. Create 4D Hilbert space vectors via Kronecker Tensor Products
        self.ket_00 = np.kron(self.ket_0, self.ket_0)
        self.ket_11 = np.kron(self.ket_1, self.ket_1)

        # 3. The Bell State |Phi+> = 1/sqrt(2) * (|00> + |11>)
        self.bell_phi_plus = (1 / math.sqrt(2)) * (self.ket_00 + self.ket_11)

        # 4. Pauli Matrices for measurement observables
        self.sigma_z = np.array([[1, 0],
                                 [0, -1]])
        self.sigma_x = np.array([[0, 1],
                                 [1, 0]])

        # 5. Optimal Measurement Angles for Alice (A) and Bob (B) to maximize CHSH
        self.A = self.sigma_z
        self.A_prime = self.sigma_x
        self.B = (-1 / math.sqrt(2)) * (self.sigma_z + self.sigma_x)
        self.B_prime = (1 / math.sqrt(2)) * (self.sigma_z - self.sigma_x)

    def expectation_value(self, op1, op2, state) -> float:
        """Calculates <psi| Observable |psi> using tensor products."""
        observable = np.kron(op1, op2)
        # Dot product of the state vector with the observable matrix applied to the state
        return np.dot(state.T, np.dot(observable, state))

    def calculate_chsh_correlation(self, eavesdropper_active: bool) -> float:
        """
        Calculates the CHSH S-value dynamically using matrix algebra.
        S = E(A, B) - E(A, B') + E(A', B) + E(A', B')
        """
        if not eavesdropper_active:
            # Secure: The qubits are in perfect quantum entanglement
            state = self.bell_phi_plus
        else:
            # Hacked: Eve's measurement forces a physical state collapse.
            # The 4D entanglement breaks, collapsing into a classical 2D state (|00> or |11>)
            state = self.ket_00 if random.random() < 0.5 else self.ket_11

        # Calculate the four expectation values
        E_AB = self.expectation_value(self.A, self.B, state)
        E_ABp = self.expectation_value(self.A, self.B_prime, state)
        E_ApB = self.expectation_value(self.A_prime, self.B, state)
        E_ApBp = self.expectation_value(self.A_prime, self.B_prime, state)

        # Calculate final S-value
        S = E_AB - E_ABp + E_ApB + E_ApBp

        # Add a tiny margin of simulated thermal hardware noise (+/- 0.015) for realism
        noise = random.uniform(-0.015, 0.015)
        return abs(S) + noise

def run_soc_dashboard(duration_seconds: int = 15):
    node = EntanglementNode()
    eavesdropper_active = False

    print(f"\n{CYAN}")
    print("="*65)
    print("        ALIRO QUANTUM ENTANGLEMENT SOC DASHBOARD (E91)      ")
    print("="*65)
    print(f"{RESET}")
    print("Monitoring network nodes [Alice] <---> [Entanglement] <---> [Bob]")
    print("Initializing Bell State generator and 4D Tensor calculations... \n")
    time.sleep(1)

    print(f"{'TIME':<10} | {'NETWORK STATUS':<20} | {'CHSH S-VALUE':<17} | {'SECURITY ALERT'}")
    print("-" * 72)

    try:
        for i in range(duration_seconds):
            if i == (duration_seconds // 2):
                eavesdropper_active = True

            current_time = time.strftime("%H:%M:%S")
            s_value = node.calculate_chsh_correlation(eavesdropper_active)

            if s_value >= 2.6:
                status = f"{GREEN}SECURE (Entangled){RESET}"
                alert = f"{GREEN}NONE - Link Verified{RESET}"
                s_display = f"{GREEN}{s_value:.3f}{RESET}"
            else:
                status = f"{RED}Critical (Collapsed){RESET}"
                alert = f"{RED}INTRUSION DETECTED (Eve){RESET}"
                s_display = f"{RED}{s_value:.3f}{RESET}"

            sys.stdout.write(f"\r{current_time:<10} | {status:<29} | S = {s_display:<24} | {alert}")
            sys.stdout.flush()
            time.sleep(1)

            if eavesdropper_active and i == (duration_seconds // 2):
                time.sleep(0.5)

    except KeyboardInterrupt:
        print(f"\n{YELLOW}[SYSTEM] Monitoring manually terminated.{RESET}")
        sys.exit()

    print(f"\n\n{YELLOW}============================================================{RESET}")
    print(f"{YELLOW}[LOG] Simulation complete. Entanglement monogamy compromised.{RESET}")
    print(f"{YELLOW}============================================================{RESET}\n")

if __name__ == "__main__":
    run_soc_dashboard()