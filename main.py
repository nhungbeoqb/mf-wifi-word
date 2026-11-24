#!/usr/bin/env python3
"""One Word for Your Wi-Fi: Breadcrumbing.

The entry writes a single word to /output/entry.txt. The word names the
one-bar-at-a-time way home Wi-Fi keeps you hoping: it dribbles out just
enough signal to keep the page loading and never enough to finish it,
like someone breadcrumbing a conversation. Funny at once, true of every
home network, and not a word anyone else reaches for first.
"""

import os

WORD = "Breadcrumbing"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 20 characters,
# not only white space, and the brief is one word. Refuse to write
# anything that would fail it instead of shipping a bad entry.
assert WORD and len(WORD) <= 20 and WORD.split() == [WORD], (
    "word fails the gate: %r" % WORD
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
