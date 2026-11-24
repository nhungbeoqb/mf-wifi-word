# One Word for Your Wi-Fi — Breadcrumbing

Entry for the make.fun bounty
[One Word for Your Wi-Fi](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
($2, one word, funniest and most accurate wins).

## The word

**Breadcrumbing.**

Home Wi-Fi dribbles out one bar at a time: just enough signal to keep
the page loading, never enough to finish it. It keeps you hoping, the
way someone breadcrumbing a conversation keeps you waiting on the next
crumb of a reply. Funny at once, true of every home network, and not a
word anyone else reaches for first.

## How it works

`main.py` (Python 3 stdlib only, no network) writes the single word to
`/output/entry.txt` — 13 characters, one word, no trailing newline —
and refuses to write anything that would fail the competition gate
(1–20 characters, not only whitespace).

Run it twice and the output is byte-identical
(sha256 `4ebdc7b9e5dd1ef1f6e0211d1af4c243085ae45e05967700df50036b6a58af37`).

## License

MIT — see `LICENSE`.
