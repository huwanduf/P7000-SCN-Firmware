import hashlib
from pathlib import Path
p=Path(__file__).resolve().parent/"firmware/firmware.bin"
assert hashlib.sha256(p.read_bytes()).hexdigest()=="f69fb7f30de084eee24d4c6a98ae51727192f98af1cad286bba81e26f942cdd6"
print("PASS: v3.2.2 firmware SHA-256")
