import math
import random
import secrets
from typing import List, Tuple

class Bob:
    """Represents the receiver in the BB84 QKD(Quantum Key Distribution) protocol."""

    def __init__(self, bit_length: int = 100):
        self.bit_length: int = bit_length
        self.chosen_bases: List[str] = []
        self.measured_bits: List[int] = []

    def generate_bases(self) -> List[str]:
        """Randomly assigns a measurement basis ('+' or 'x') for each incoming photon."""
        bases = ['+', 'x']
        self.chosen_bases = [secrets.choice(bases) for _ in range(self.bit_length)]
        return self.chosen_bases

    def measure_photons(self, photons: List[Tuple[float, float]]) -> List[int]:
        """
        Measures incoming quantum state vectors using quantum probability collapse,
        completely independent of what Alice originally sent.
        """
        inv_sqrt_2 = 1.0 / math.sqrt(2.0)
        self.measured_bits = []

        for photon, bob_basis in zip(photons, self.chosen_bases):
            x, y = photon

            if bob_basis == '+':
                # Rectilinear measurement: probability of measuring |0> or x^2
                prob_zero = x ** 2
                if random.random() < prob_zero:
                    self.measured_bits.append(0)
                else:
                    self.measured_bits.append(1)
            elif bob_basis == 'x':
                # Diagonal measurement: inner product projection onto |+> state
                amplitude_plus = inv_sqrt_2 * (x + y)
                prob_plus = amplitude_plus ** 2
                prob_plus = max(0.0, min(1.0, prob_plus))

                if random.random() < prob_plus:
                    self.measured_bits.append(0)
                else:
                    self.measured_bits.append(1)

        return self.measured_bits