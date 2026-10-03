"""Keep asking for a word until the user types bye."""


def main() -> None:
    while True:
        word = input("Type a word: ")
        if word == "bye":
            break
        if word == "":
            continue
        print(word)


if __name__ == "__main__":
    main()
