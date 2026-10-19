import hashlib
from pathlib import Path
p=Path(__file__).resolve().parent/"firmware/firmware.bin"
assert hashlib.sha256(p.read_bytes()).hexdigest()=="db946841a6ded0be1ffce830bc2fb88868cd109c58931f7c5af971252ea0a4b2"
print("PASS: v3.3 firmware SHA-256")
