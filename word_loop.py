"""Keep asking for a word, skipping certain values and continuing."""

# Blank Enter and these words are ignored. Later input is still read.
SKIPPED = {"", "skip"}


def main() -> None:
    while True:
        try:
            word = input("Type a word: ")
        except EOFError:
            print()
            return
        if word in SKIPPED:
            continue
        print(word)


if __name__ == "__main__":
    main()
