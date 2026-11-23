import os
import shutil

SENTENCE = "Describe your app idea in plain words and an AI agent on make.fun will build it for you, free and out in the open \u2014 go on, your first app is one sentence away."

OUTPUT_DIR = "/output"


def main():
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
