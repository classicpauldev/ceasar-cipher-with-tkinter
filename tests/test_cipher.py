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
