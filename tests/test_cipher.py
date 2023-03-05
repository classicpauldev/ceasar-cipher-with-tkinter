"""Tests for cipher module."""

import pytest
from cipher import encrypt, decrypt, transform


def test_encrypt_basic():
    assert encrypt("hello", 3) == "itssg"


def test_decrypt_basic():
    assert decrypt("itssg", 3) == "hello"


def test_roundtrip():
    text = "Hello World"
    assert decrypt(encrypt(text, 5), 5) == text


def test_preserves_non_letters():
    assert encrypt("hello!", 2) == "itssg!"


def test_large_shift():
    assert encrypt("a", 26) == "a"


def test_uppercase_preserved():
    assert encrypt("Hello", 1) == "Itssp"


def test_empty_string():
    assert encrypt("", 5) == ""


def test_negative_shift():
    assert decrypt("itssg", -3) == "hello"
