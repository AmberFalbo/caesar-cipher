from caesar_cipher.caesar_cipher import encrypt, decrypt, crack
from caesar_cipher import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_shift_by_one():
    actual = encrypt("cat", 1)
    expected = "dbu"
    assert actual == expected

def test_encrypt_shift_by_two():
    actual = encrypt("cat", 2)
    expected = "ecv"
    assert actual == expected

def test_encrypt_shift_by_two_plus_number():
    actual = encrypt("cat 1", 2)
    expected = "ecv 1"
    assert actual == expected
