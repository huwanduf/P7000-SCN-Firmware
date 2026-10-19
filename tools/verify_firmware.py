#!/usr/bin/env python3
"""Verify the current downloaded image without camera/SD access."""
import hashlib,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
path=Path(sys.argv[1])if len(sys.argv)>1 else root/'firmware/firmware.bin'
expected=(root/'SHA256SUMS').read_text().split()[0]
actual=hashlib.sha256(path.read_bytes()).hexdigest()
if actual!=expected:raise SystemExit('FAIL: firmware SHA-256 mismatch')
print('PASS: '+actual)
