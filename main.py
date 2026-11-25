#!/usr/bin/env python3
"""Write the absurd terms-of-service clause to entry.txt.

Competition: The Absurd Clause Contest (one original English
sentence, 1-200 chars, phrased as a clause buried deep inside a
terms-of-service agreement; the brief rewards, in order, being
on subject, a joke that lands on one reading with no outside
setup, real legal-boilerplate register until the absurdity
hits, an original specific concrete image, and tight writing).
Candidates:
A) "Clause 31.2: You grant us a perpetual, irrevocable licence
   to your left sock, which we may collect without notice and
   pair only with socks lost by other users before 2019."
B) "Section 14.7: By continuing to breathe within 500 metres
   of this app, you agree that any sneeze may be recorded,
   remixed, and performed by our legal team at the office
   Christmas party."
C) "Clause 9.3: If you read this clause aloud, you have
   accepted it; if you read it silently, you have accepted it
   twice, and our parrot, who witnessed both, accepts no
   appeals."
D) "Section 22.4(b): In the event of a zombie apocalypse,
   your subscription will auto-renew, and cancellation
   requests must be submitted in person, in triplicate, to
   the zombies."
Selected A: 'perpetual, irrevocable licence' is genuine ToS
language, so the boilerplate register holds longest before
the left sock lands, and the pairing rule (only with socks
lost by other users before 2019) is concrete and specific.
B is funny but broader and less legal in phrasing; C's parrot
breaks the register early; D uses a well-worn zombie setup.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Clause 31.2: You grant us a perpetual, irrevocable licence to your left sock, which we may collect without notice and pair only with socks lost by other users before 2019."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    # Revision: enforce exactly one clean sentence line within
    # the gate limit, so the entry is exactly the selected text.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")
    if not body.endswith("."):
        raise ValueError("entry must end as one sentence")


def main() -> None:
    validate(TEXT)
    # Write bytes directly so the entry is identical on every run.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
