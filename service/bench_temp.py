# 78803612 - id успешной попытки


def get_score(keys, all_symbols, valid_characters="123456789", players=2):
    return sum(
        0 != all_symbols.count(character) <= players * keys
        for character in valid_characters
    )


def call_main(file_path):
    print(
        get_score(
            keys=int(file_path.readline().rstrip()),
            all_symbols=f"{file_path.readline().rstrip()}{file_path.readline().rstrip()}{file_path.readline().rstrip()}{file_path.readline().rstrip()}",
        )
    )
