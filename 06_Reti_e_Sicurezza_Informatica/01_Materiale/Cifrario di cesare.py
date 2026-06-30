def encrypt_char(char: str, key: int) -> str:
    if char.isupper():
        return chr((ord(char) - 65 + key) % 26 + 65)
    elif char.islower():
        return chr((ord(char) - 97 + key) % 26 + 97)
    return char


def encrypt(text: str, key: int) -> str:
    result = ''
    for char in text:
        result += encrypt_char(char, key)
    return result


def main():
    action = input("Vuoi (c)ifrare o (d)ecifrare? ").strip().lower()
    if action not in ('c', 'd'):
        print("Scelta non valida.")
        return

    text = input("Inserisci il testo: ")
    key = int(input("Inserisci la chiave: "))

    if action == 'd':
        key = -key

    result = encrypt(text, key)
    print(f"Risultato: {result}")


if __name__ == '__main__':
    main()