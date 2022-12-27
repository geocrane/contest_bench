def get_score(keys, all_symbols, valid_characters="123456789", players=2):
    return sum(
        0 != all_symbols.count(character) <= players * keys
        for character in valid_characters
    )


if __name__ == "__main__":
    print(
        get_score(
            keys=int(input()),
            all_symbols=f"{input()}{input()}{input()}{input()}",
        )
    )
