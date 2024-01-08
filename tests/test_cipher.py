"""Tests for cipher module."""

import pytest

# Cipher module unit tests
from cipher import encrypt, decrypt, transform


def test_encrypt_basic():
    assert encrypt("hello", 3) == "lyccs"


def test_decrypt_basic():
    assert decrypt("lyccs", 3) == "hello"


def test_roundtrip():
    text = "Hello World"
    assert decrypt(encrypt(text, 5), 5) == text


def test_preserves_non_letters():
    assert encrypt("hello!", 2) == "ktxxa!"


def test_preserves_spaces():
    assert encrypt("hi there", 1) == "jo yjrtr"


def test_zero_shift_identity():
    assert encrypt("hello", 0) == "hello"


def test_large_shift():
    assert encrypt("a", 26) == "a"


def test_uppercase_preserved():
    assert encrypt("Hello", 1) == "Jrzzp"


def test_empty_string():
    assert encrypt("", 5) == ""


def test_negative_shift():
    """Decrypt text that was encrypted with a negative shift."""
    encrypted = encrypt("hello", -3)
    assert decrypt(encrypted, -3) == "hello"


def test_shift_13_roundtrip():
    """ROT13-style: encrypting twice with shift 13 returns original."""
    text = "secret message"
    assert decrypt(encrypt(text, 13), 13) == text
