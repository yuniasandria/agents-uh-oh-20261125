"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

Word: Fumbling (8 chars). A helpless, human blurt: the agent is fumbling
for an answer it does not have. Same -ing gerund form as the board's
familiar stall words, but a fresh, instantly readable confession that no
visible entrant uses.
"""

import os

WORD = "Fumbling"


def main():
    # PART_A
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 99
    assert WORD == WORD.strip()
    assert len(WORD.split()) == 1
    assert "\n" not in WORD and "\r" not in WORD
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    # PART_B: verify what was actually written before exiting.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert text == WORD + "\n", "entry.txt must be exactly the word plus newline"
    assert 1 <= len(WORD) <= 99
    assert len(text.strip().split()) == 1
    assert text.count("\n") == 1


if __name__ == "__main__":
    main()
