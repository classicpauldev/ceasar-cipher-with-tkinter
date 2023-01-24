"""Caesar cipher encoding and decoding."""

ALPHABET = "qwertyuiopasdfghjklzxcvbnm"
ALPHABET_SIZE = len(ALPHABET)


def transform(text: str, shift: int) -> str:
    """Apply Caesar cipher transformation."""
    result = ""
    for letter in text:
        if letter.isupper():
            if letter.lower() in ALPHABET:
                idx = (ALPHABET.index(letter.lower()) + shift) % len(ALPHABET)
                result += ALPHABET[idx].upper()
        elif letter in ALPHABET:
            idx = (ALPHABET.index(letter) + shift) % len(ALPHABET)
            result += ALPHABET[idx]
        else:
            result += letter
    return result
