import sys
import time
from bb84.alice import Alice
from bb84.bob import Bob
from bb84.eve import Eve

def run_bb84_simulation(eavesdropper_active: bool = True):
    # ANSI color codes for a high-tech terminal look
    BLUE = "\033[94m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Clean, simple bordered header
    print(f"""{BLUE}
    ==================================================
           BB84 QUANTUM KEY DISTRIBUTION SIMULATOR
    ==================================================
    {RESET}""")

    print(f"Eavesdropper (Eve) Active: {RED if eavesdropper_active else GREEN}{eavesdropper_active}{RESET}\n")
    
    bit_count = 20  # Smaller count for a clean visual display
    alice = Alice(bit_length=bit_count)
    bob = Bob(bit_length=bit_count)
    eve = Eve(bit_length=bit_count) if eavesdropper_active else None

    # 1. Alice prepares and encodes
    alice.generate_raw_bits()
    alice.generate_bases()
    photons = alice.encode_photons()

    print(f"{GREEN}[Alice]{RESET} Generated {bit_count} random bits and polarized photons.")

    # Simulated transmission delay animation
    print(f"{BLUE}[Transmission]{RESET} Fusing photons into fiber-optic line", end="")
    for _ in range(3):
        time.sleep(0.2)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(" [SENT]\n")

    # 2. Transmission phase (Intercepted by Eve if active)
    if eve:
        eve.generate_bases()
        print(f"{RED}[Eve]  Intercepting fiber-optic line... measuring states.{RESET}")
        photons = eve.intercept_and_measure(photons)
        time.sleep(0.3)

    # 3. Bob generates bases and measures
    bob.generate_bases()
    bob.measure_photons(photons)
    print(f"{BLUE}[Bob]  Configured detection filters and measured incoming stream.{RESET}\n")

    # Visual Pipeline Table Header
    print(f"{'Qubit':<6} | {'Alice Bit':<10} | {'Alice Basis':<12} | {('Eve Basis' if eve else ''):<12} | {'Bob Basis':<10} | {'Status':<10}")
    print("-" * 68)

    sifted_alice_key = []
    sifted_bob_key = []

    for i in range(bit_count):
        a_bit = alice.raw_bits[i]
        a_base = alice.chosen_bases[i]
        e_base = eve.chosen_bases[i] if eve else "-"
        b_base = bob.chosen_bases[i]
        
        match = (a_base == b_base)
        status = f"{GREEN}Kept{RESET}" if match else f"{YELLOW}Discarded{RESET}"
        
        if match:
            sifted_alice_key.append(a_bit)
            sifted_bob_key.append(bob.measured_bits[i])

        print(f"#{i:<5} | {a_bit:<10} | {a_base:<12} | {str(e_base):<12} | {b_base:<10} | {status}")

    # 4. Calculate Error Rate (QBER)
    errors = sum(1 for a, b in zip(sifted_alice_key, sifted_bob_key) if a != b)
    qber = (errors / len(sifted_alice_key)) if sifted_alice_key else 0.0

    print("-" * 68)
    print(f"Sifted Key Length: {len(sifted_alice_key)} bits")
    print(f"Mismatched Bits Found: {errors}")
    print(f"Quantum Bit Error Rate (QBER): {qber * 100:.2f}%")

    if qber > 0.11:
        print(f"\n{RED}[SECURITY ALERT] High error rate detected (>11%). Eavesdropper present! Aborting.{RESET}")
    else:
        print(f"\n{GREEN}[SUCCESS] Secure key successfully established with 0% error rate.{RESET}")

if __name__ == "__main__":
    run_bb84_simulation(eavesdropper_active=False)
    time.sleep(1)
    print("\n" + "="*70 + "\n")
    run_bb84_simulation(eavesdropper_active=True)