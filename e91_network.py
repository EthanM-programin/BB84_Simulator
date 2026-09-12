import time
import math
import random
import sys

# ANSI Color Codes for SOC Dashboard
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class EntanglementNode:
    """Simulates a central quantum network node distributing Bell pairs."""
    def __init__(self):
        self.active_pair = 0

    def calculate_chsh_correlation(self, eavesdropper_active: bool) -> float:
        """
        Simulates the CHSH S-value based on Bell's Inequality.
        A secure entangled network yields S = 2.828.
        A compromised network collapses to S <= 2.0.
        """

        # Quantum Maximum is 2 * sqrt(2) = 2.828
        quantum_max = 2.828

        if not eavesdropper_active:
            # Secure network: slight variations due to simulated hardware noise
            noise = random.uniform(-0.05, 0.02)
            return quantum_max + noise
        else:
            # Compromised network: Entanglement broken, collapses to classical probability
            classical_limit = random.uniform(1.30, 1.85)
            return classical_limit

def run_soc_dashboard(duration_seconds: int = 15):
    node = EntanglementNode()
    eavesdropper_active = False

    print(f"\n{CYAN}")
    print("="*60)
    print("=     ALIRO QUANTUM ENTANGLEMENT SOC DASHBOARD (E91)     ")
    print("="*60)
    print(f"{RESET}")
    print("Monitoring network nodes [Alice] <---> [Entanglement] <---> [Bob]")
    print("Initializng Bell State generator... \n")
    time.sleep(1)

    print(f"{'TIME':<10} | {'NETWORK STATUS':<20} | {'CHSH S-VALUE':<17} | {'SECURITY ALERT'}")
    print("-" * 65)

    try:
        for i in range(duration_seconds):
            # Inject a man-in-the-middle attack halfway through the simulation
            if i == (duration_seconds // 2):
                eavesdropper_active = True

            current_time = time.strftime("%H:%M:%S")
            s_value = node.calculate_chsh_correlation(eavesdropper_active)

            # Dashboard Logic
            if s_value >= 2.6:
                status = f"{GREEN}SECURE (Entangled){RESET}"
                alert = f"{GREEN}NONE - Link Verified{RESET}"
                s_display = f"{GREEN}{s_value:.3f}{RESET}"
            else:
                status = f"{RED}CRITICAL (Collapsed){RESET}"
                alert = f"{RED}INTRUSION DETECTED (Eve){RESET}"
                s_display = f"{RED}{s_value:.3f}{RESET}"

            # Print dashboard row
            sys.stdout.write(f"\r{current_time:<10} | {status:<29} | S = {s_display:<22} | {alert}")
            sys.stdout.flush()

            # Simulate real-time monitoring tick
            time.sleep(1)

            # If hacked, lock the terminal for a moment to emphasize the drop
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