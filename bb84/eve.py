import math
import random
import secrets
from typing import List, Tuple

class Eve:
    """Represents the eavesdropper (intercept-resend attacker) in the BB84 protocol."""

    def __init__(self, bit_length: int = 100):
        self.bit_length: int = bit_length
        self.chosen_bases: List[str] = []
        self.intercepted_bits: List[int] = []

    def generate_bases(self) -> List[str]:
        """Randomly assigns a measurement basis ('+' or 'x') for each intercepted photon."""
        bases = ['+', 'x']
        self.chosen_bases = [secrets.choice(bases) for _ in range(self.bit_length)]
        return self.chosen_bases

    def intercept_and_measure(self, photons: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """
        Intercepts photons, measures them using quantum state probabilities,
        and forwards the newly collapsed state vectors to Bob.
        """
        inv_sqrt_2 = 1.0 / math.sqrt(2.0)
        modified_photons = []
        self.intercepted_bits = []

        for photon, eve_basis in zip(photons, self.chosen_bases):
            x, y = photon

            if eve_basis == '+':
                prob_zero = x ** 2
                if random.random() < prob_zero:
                    self.intercepted_bits.append(0)
                    modified_photons.append((1.0, 0.0))
                else:
                    self.intercepted_bits.append(1)
                    modified_photons.append((0.0, 1.0))

            elif eve_basis == 'x':
                amplitude_plus = inv_sqrt_2 * (x + y)
                prob_plus = amplitude_plus ** 2
                prob_plus = max(0.0, min(1.0, prob_plus))

                if random.random() < prob_plus:
                    self.intercepted_bits.append(0)
                    modified_photons.append((inv_sqrt_2, inv_sqrt_2))
                else:
                    self.intercepted_bits.append(1)
                    modified_photons.append((inv_sqrt_2, -inv_sqrt_2))

        return modified_photons