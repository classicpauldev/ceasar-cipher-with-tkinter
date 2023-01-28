"""Caesar cipher encoding and decoding."""

ALPHABET = "qwertyuiopasdfghjklzxcvbnm"
ALPHABET_SIZE = len(ALPHABET)


def transform(text: str, shift: int) -> str:
    """Apply Caesar cipher transformation."""
    result = ""
    for letter in text:
        if letter.isupper():
            if letter.lower() in ALPHABET:
                idx = (ALPHABET.index(letter.lower()) + shift) % ALPHABET_SIZE
                result += ALPHABET[idx].upper()
        elif letter in ALPHABET:
            idx = (ALPHABET.index(letter) + shift) % ALPHABET_SIZE
            result += ALPHABET[idx]
        else:
            result += letter
    return result


def encrypt(text: str, shift: int) -> str:
    """Encrypt text with Caesar cipher."""
    return transform(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text with Caesar cipher."""
    return transform(text, -shift)
