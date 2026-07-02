"""Firma un release JSON con la chiave privata Ed25519.

Uso:
    python sign_release_json.py --key ~/.ssh/ehub-release-signing.pem \\
        manager-version.json

Rimuove il campo 'signature' esistente, canonicalizza (JSON compatto, chiavi
sorted, UTF-8), firma con Ed25519 via `openssl pkeyutl -sign -rawin`, riscrive
il file aggiungendo il nuovo campo 'signature' (base64).

La public key corrispondente e' hardcoded in `ehub-manager/update_service.py`
come `RELEASE_SIGNING_PUBKEY_PEM`. Se ruoti la keypair, aggiorna li'.

Richiede solo `openssl` disponibile nel PATH.
"""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import tempfile
from pathlib import Path

_SIGNATURE_FIELD = "signature"


def _canonical_bytes(payload: dict) -> bytes:
    clean = {k: v for k, v in payload.items() if k != _SIGNATURE_FIELD}
    return json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sign(payload_bytes: bytes, key_path: Path) -> str:
    with tempfile.TemporaryDirectory() as td:
        pl = Path(td) / "payload.bin"
        pl.write_bytes(payload_bytes)
        sig_file = Path(td) / "sig.bin"
        cmd = [
            "openssl", "pkeyutl", "-sign",
            "-inkey", str(key_path),
            "-rawin", "-in", str(pl),
            "-out", str(sig_file),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if r.returncode != 0:
            raise RuntimeError(f"openssl sign fallito: {r.stderr.strip()}")
        sig = sig_file.read_bytes()
    return base64.b64encode(sig).decode("ascii")


def main() -> None:
    ap = argparse.ArgumentParser(description="Firma un release JSON con Ed25519.")
    ap.add_argument("--key", required=True, help="Path della private key PEM (Ed25519)")
    ap.add_argument("json_file", help="Path del release JSON da firmare (viene modificato in place)")
    args = ap.parse_args()

    key_path = Path(args.key).expanduser()
    if not key_path.exists():
        print(f"ERRORE: chiave non trovata: {key_path}", file=sys.stderr)
        sys.exit(2)
    jp = Path(args.json_file)
    if not jp.exists():
        print(f"ERRORE: JSON non trovato: {jp}", file=sys.stderr)
        sys.exit(2)

    data = json.loads(jp.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        print("ERRORE: il release JSON deve essere un oggetto", file=sys.stderr)
        sys.exit(2)

    signature = sign(_canonical_bytes(data), key_path)
    data[_SIGNATURE_FIELD] = signature

    # Reindento a 2 spazi per leggibilita' git-diff, ma la verifica va sul
    # payload canonicalizzato senza signature (l'indentazione non conta).
    jp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: {jp} firmato ({signature[:16]}...)")


if __name__ == "__main__":
    main()
