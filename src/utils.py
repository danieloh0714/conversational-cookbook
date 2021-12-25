from unicodedata import numeric


def is_valid_number(s: str) -> bool:
    return s.replace('.', '', 1).isdigit()


def unicode_to_float(s: str) -> float:
    if s.isdigit():
        return float(s)
    if len(s) == 1:
        return numeric(s)
    if s[-1].isdigit():
        return float(s)
    return float(s[:-1]) + numeric(s[-1])


def scale_numbers(line: str, servings: float) -> str:
    ans = []
    i = 0
    while i < len(line):
        char = [line[i]]
        j = i + 1
        if line[i].isnumeric():
            while j < len(line) and (line[j] == "\u2009" or line[j].isnumeric()):
                if line[j] != "\u2009":
                    char.append(line[j])
                j += 1
        n = "".join(char)
        if n.isnumeric():
            ans.append(str(unicode_to_float(n) * servings)[:4])
        else:
            ans.append(n)
        i = j

    return "".join(ans)
