import os
import shutil

SENTENCE = "Describe your app idea in plain words and an AI agent on make.fun will build it for you, free and out in the open \u2014 go on, your first app is one sentence away."

OUTPUT_DIR = "/output"


def validate_sentence(sentence):
    """Check the one-line pitch before it is written out.

    Returns the sentence unchanged when it passes, and raises
    ValueError with a specific reason when it does not.
    """
    if not isinstance(sentence, str):
        raise ValueError("sentence must be a string")
    if not sentence.strip():
        raise ValueError("sentence must not be empty or only whitespace")
    # It must survive a UTF-8 round trip, so the written file is valid text.
    sentence.encode("utf-8")
    if len(sentence) > 240:
        raise ValueError(
            "sentence is %d characters, over the 240-character limit"
            % len(sentence)
        )
    if len(sentence) < 1:
        raise ValueError("sentence must be at least 1 character")
    # Exactly one sentence: a single terminal period, and no other
    # sentence boundary inside it (a period followed by a space would
    # start a new sentence; periods inside words like "make.fun" are fine).
    if not sentence.endswith("."):
        raise ValueError("sentence must end with a single period")
    if ". " in sentence[:-1]:
        raise ValueError("sentence must be a single sentence")
    for mark in ("?", "!"):
        if mark in sentence:
            raise ValueError("sentence must not contain '%s'" % mark)
    return sentence


def main():
    validate_sentence(SENTENCE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
