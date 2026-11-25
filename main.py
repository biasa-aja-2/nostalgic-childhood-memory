"""Write one nostalgic childhood-memory sentence to /output/entry.txt.

Pure Python standard library only.
"""

import os

SENTENCE = (
    "The night of the lunar eclipse, my father let me stay up past bedtime, "
    "and I fell asleep on his lap with the moon half-gone, waking up sure "
    "the sky had kept a secret just for us."
)


def main() -> None:
    text = SENTENCE.strip()
    assert text, "sentence must not be empty"
    assert len(text) <= 280, f"sentence is {len(text)} chars, over the 280 cap"
    assert text.count(".") == 1 and text.endswith("."), "must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
