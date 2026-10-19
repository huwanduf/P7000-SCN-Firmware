import hashlib
from pathlib import Path
p=Path(__file__).resolve().parent/"firmware/firmware.bin"
assert hashlib.sha256(p.read_bytes()).hexdigest()=="1e34e288900e954c20cca7821475f1accb0118ff91047894d3820ca8c055933d"
print("PASS: v2 firmware SHA-256")
