import hashlib
from pathlib import Path
p=Path(__file__).resolve().parent/"firmware/firmware.bin"
assert hashlib.sha256(p.read_bytes()).hexdigest()=="db51086dd9d823e6819307aecda22873e4c9b73cc03bb33345b5d91c287facd7"
print("PASS: v1 firmware SHA-256")
