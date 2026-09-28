"""Poseidon Algebraic Hash Function Engine.
100% Python Standard Library.
"""

class PoseidonHash:
    """Poseidon zero-knowledge friendly hash with S-boxes and MDS matrix."""
    PRIME = 2147483647

    def __init__(self, state_size=3):
        self.t = state_size
        self.mds = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]

    def _sbox(self, x):
        return pow(x, 5, self.PRIME)

    def hash(self, inputs):
        state = list(inputs[:self.t]) + [0] * max(0, self.t - len(inputs))
        for _ in range(3):
            state = [self._sbox(s) for s in state]
            new_state = [0] * self.t
            for i in range(self.t):
                for j in range(self.t):
                    new_state[i] = (new_state[i] + self.mds[i][j] * state[j]) % self.PRIME
            state = new_state
        return state[0]
