import pytest
from phonebook import PhoneBook

@pytest.fixture()
def phonebook(tmpdir):
    phonebook = PhoneBook(tmpdir)
    yield phonebook
    phonebook.clear()

def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")

def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("MissingName")

def test_empty_phonebook_is_consistent(phonebook):
    assert phonebook.is_consistent()

def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Anna", "012345")
    assert phonebook.is_consistent()

def test_is_inconsistent_with_duplicate_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "12345")
    assert phonebook.is_consistent() == False

def test_is_inconsistent_with_duplicate_prefix(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "123")
    assert phonebook.is_consistent() == False

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in  phonebook.names()

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")