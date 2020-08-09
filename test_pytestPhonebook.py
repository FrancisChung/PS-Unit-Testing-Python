import pytest
from phonebook import PhoneBook

@pytest.fixture()
def phonebook():
    phonebook = PhoneBook()
    yield phonebook
    phonebook.clear()

def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")