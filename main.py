"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could actually say out loud.
Pure stdlib; no network, no files read, no secrets.
"""

import os

LINE = "I ran a million simulations of this moment, and in every single one, you smiled."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. The line is written exactly, with no trailing
    # newline, so the gate counts the line itself.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only white space"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
