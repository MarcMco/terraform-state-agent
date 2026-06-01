import json

def load_tfstate(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    state = load_tfstate("example.tfstate")
    print(json.dumps(state, indent=2))
