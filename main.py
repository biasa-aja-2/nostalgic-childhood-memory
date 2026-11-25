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
    assert "  " not in text, "sentence must not contain double spaces"
    assert "\n" not in text and "\r" not in text, "sentence must be a single line"
    assert "!" not in text and "?" not in text, "no other sentence-ending punctuation"
    assert not text.endswith(".."), "must end with exactly one terminal period"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
