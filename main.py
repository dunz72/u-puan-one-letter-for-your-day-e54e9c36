"""One Letter for Your Day -- entry program.

Writes exactly one letter, "Z", to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset).

The letter stands for the hidden word "zero sleep": the day behind
this entry was spent awake through the night, hunting bounties at
04:34 WIB with no sleep at all.

Standard library only. Deterministic: no network, no randomness, no
clock. The output is a single byte, with no trailing newline and no
BOM.
"""

import os

LETTER = "Z"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LETTER.encode("ascii")
    if len(data) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        raise ValueError("entry must be exactly one uppercase letter A-Z")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and prove the file on disk is exactly that one letter:
    # one byte, one uppercase A-Z character, nothing else.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("entry.txt does not contain exactly one letter A-Z")


if __name__ == "__main__":
    main()
