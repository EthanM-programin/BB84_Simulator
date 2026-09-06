import math
import secrets
from typing import List, Tuple

class Alice:
    """Represents the sender in the BB84 QKD(Quantum Key Distribution) protocol."""

    def __init__(self, bit_length: int = 100):
        if bit_length <= 0:
            raise ValueError("Bit length must be a positive integer.")

        self.bit_length: int = bit_length
        self.raw_bits: List[int] = []
        self.chosen_bases: List[str] = []
        self.enconded_photons: List[Tuple[float, float]] = []

    def generate_raw_bits(self) -> List[int]:
        """Generates a cryptographically secure sequence of random 0s and 1s."""
        self.raw_bits = [secrets.randbelow(2) for _ in range(self.bit_length)]
        return self.raw_bits 

    def generate_bases(self) -> List[str]:
        """Randomly assigns a measurement basis ('+' or 'x') for each bit."""
        bases = ['+', 'x']
        self.chosen_bases = [secrets.choice(bases) for _ in range(self.bit_length)]
        return self.chosen_bases 

    def encode_photons(self) -> List[Tuple[float, float]]:
        """
        Translates raw bits and chosen bases into 2D quantum state vectors.
        Uses zip() to iterate through both lists simultaneously.
        """
        inv_sqrt_2 = 1.0 / math.sqrt(2.0)
        self.encoded_photons = []

        for bit, basis in zip(self.raw_bits, self.chosen_bases):
            if basis == '+':
                if bit == 0:
                    self.encoded_photons.append((1.0, 0.0)) # |0> state
                else:
                    self.encoded_photons.append((0.0, 1.0)) # |1> state
            elif basis == 'x':
                if bit == 0:
                    self.encoded_photons.append((inv_sqrt_2, inv_sqrt_2)) # |+> state
                else:
                    self.encoded_photons.append((inv_sqrt_2, -inv_sqrt_2)) # |-> state

        return self.encoded_photons