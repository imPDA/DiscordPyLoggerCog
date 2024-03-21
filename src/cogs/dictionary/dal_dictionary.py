import re


def read_dictionary(path) -> dict[str, dict]:
    with open(path, "r", encoding="windows-1251") as f:
        file = f.read()

    dictionary = {}
    letter = ""
    skipped = []
    for part in file.split("\n\n"):
        if len(part) == 1:
            letter = part
            dictionary[letter] = {}
        else:
            res = re.findall(r"^([А-Я-]+)[ ,?]", part)

            if not res:
                skipped.append(part)
                continue

            term = res[0]
            dictionary[letter][term] = part

    # print(f"Skipped {len(skipped)} parts")
    return dictionary
