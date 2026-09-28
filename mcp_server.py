import sys
import json
from client import PoseidonHash

hasher = PoseidonHash(state_size=3)

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "poseidon_hash",
                        "description": "Compute ZK-friendly Poseidon algebraic hash digest over integer inputs",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "inputs": {"type": "array", "items": {"type": "integer"}}
                            },
                            "required": ["inputs"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "poseidon_hash":
            d = hasher.hash(args["inputs"])
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"hash": d})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
