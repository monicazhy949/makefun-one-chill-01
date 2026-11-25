"""One Line, One Chill — a single sentence of horror, under 200 characters."""

import os

ENTRY = "The voicemail from my dead grandmother ended with her whispering my new address, the one I moved to yesterday."


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
