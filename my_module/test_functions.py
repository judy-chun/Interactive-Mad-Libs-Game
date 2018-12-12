"""Tests for two of my functions: remove_punct, password_encryption.
This tests that the remove_punct function executes, and returns a string with removed punctuation, as expected.
This also tests that the password_encryption function executes, and returns a encrypted string, as expected. 
"""


# Imports 
from functions import remove_punct, password_encryption 


# Testing remove_punct function with following inputs 
def test_remove_punct():

    assert callable(remove_punct)
    assert remove_punct("Hi! This is really cool, fun, and awesome!?*?!") == "Hi This is really cool fun and awesome"
    assert remove_punct("!?**!!") == ""


# Testing password_encryption function with following inputs 
def test_password_encryption():

    assert callable(password_encryption)
    assert password_encryption("hello world") == "þûĂĂą¶čąĈĂú"
    assert password_encryption("i love python") == "ÿ¶ĂąČû¶ĆďĊþąĄ"
