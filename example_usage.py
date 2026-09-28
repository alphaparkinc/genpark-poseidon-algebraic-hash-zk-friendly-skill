from client import PoseidonHash

hasher = PoseidonHash(state_size=3)
digest = hasher.hash([123, 456])
print(f"Poseidon Hash Digest: {digest}")
