# import unittest
# import pytest
# from phonebook import PhoneBook
#
#
# class PhoneBookTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.phonebook = PhoneBook()
#
#     def tearDown(self) -> None:
#         pass
#
#     def test_lookup_by_name(self):
#         self.phonebook.add("Bob", "12345")
#         number = self.phonebook.lookup("Bob")
#         self.assertEqual("12345", number)
#
#     def test_missing_name(self):
#         with self.assertRaises(KeyError):
#             self.phonebook.lookup("MissingName")
#
#     def test_empty_phonebook_is_consistent(self):
#         self.assertTrue(self.phonebook.is_consistent())
#
#     def test_is_consistent_with_different_entries(self):
#         self.phonebook.add("Bob", "12345")
#         self.phonebook.add("Anna", "012345")
#         self.assertTrue(self.phonebook.is_consistent())
#
#     def test_is_inconsistent_with_duplicate_entries(self):
#         self.phonebook.add("Bob", "12345")
#         self.phonebook.add("Sue", "12345")
#         self.assertFalse(self.phonebook.is_consistent())
#
#     def test_is_inconsistent_with_duplicate_prefix(self):
#         self.phonebook.add("Bob", "12345")
#         self.phonebook.add("Sue", "123")
#         self.assertFalse(self.phonebook.is_consistent())
#
#     def test_phonebook_contains_all_names(self):
#         self.phonebook.add("Bob", "1234")
#         assert "Bob" in  self.phonebook.names()
#
#     def test_missing_name_raises_error(self):
#         with pytest.raises(KeyError):
#             self.phonebook.lookup("Bob")

