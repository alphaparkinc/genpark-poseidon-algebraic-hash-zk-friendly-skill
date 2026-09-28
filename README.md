# Poseidon Algebraic Hash Skill

High-efficiency, zero-dependency Python implementation of the **Poseidon Algebraic Hash Function** optimized for ZK-SNARK and STARK circuits.

## Features
- **Low Algebraic Degree**: Employs \(x^5\) power S-box permutations minimizing R1CS gate constraints.
- **Maximum Distance Separable (MDS)**: Linear diffusion layers guaranteeing branch number security against differential cryptanalysis.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    State["Initial State [s0, s1, s2]"] --> SBox["Non-Linear Layer: S-Box x^5"]
    SBox --> MDS["Linear Layer: MDS Matrix Multiplication"]
    MDS --> Round["Round Counter (3 Full Rounds)"]
    Round --> Digest["Squeezed Hash Digest"]
```
