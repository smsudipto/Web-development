grid = [['' for _ in range(5)] for _ in range(5)]


def build_grid(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    text = ""

    for char in key.upper():
        if char == "J":
            char = "I"

        if char.isalpha() and char not in text:
            text += char

    for char in alphabet:
        if char not in text:
            text += char

    k = 0

    for i in range(5):
        for j in range(5):
            grid[i][j] = text[k]
            k += 1


def find_letter(char):
    if char == "J":
        char = "I"

    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j


def make_pairs(message):
    message = message.upper()
    text = ""

    for char in message:
        if char.isalpha():
            if char == "J":
                char = "I"
            text += char

    pairs = ""
    i = 0

    while i < len(text):

        first = text[i]

        if i + 1 == len(text):
            pairs += first + "X"
            i += 1

        elif text[i] == text[i + 1]:
            pairs += first + "X"
            i += 1

        else:
            pairs += first + text[i + 1]
            i += 2

    return pairs


def encrypt(message):
    pairs = make_pairs(message)
    result = ""

    for i in range(0, len(pairs), 2):

        a = pairs[i]
        b = pairs[i + 1]

        r1, c1 = find_letter(a)
        r2, c2 = find_letter(b)

        if r1 == r2:
            result += grid[r1][(c1 + 1) % 5]
            result += grid[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += grid[(r1 + 1) % 5][c1]
            result += grid[(r2 + 1) % 5][c2]

        else:
            result += grid[r1][c2]
            result += grid[r2][c1]

    return result


key = input("Enter key: ")
message = input("Enter message: ")

build_grid(key)

print("\nGrid:")

for row in grid:
    print(" ".join(row))

encrypted = encrypt(message)

print("\nOriginal  :", message)
print("Prepared  :", make_pairs(message))
print("Encrypted :", encrypted)