"""
Unittest for the addressBook module.
"""

import unittest

from src import addressBook
from src import constants


class MockConfig(object):
    def __init__(self, file_path):
        self.input_file = file_path
        self.output_file = constants.EXPORT_TEXT_FILE


class TestAddressBookWithPdfFile(unittest.TestCase):

    def setUp(self):
        mockConfig = MockConfig('mock_file.pdf')
        self.book = addressBook.AddressBook(mockConfig)

    def test_importRaises(self):
        self.assertEquals(self.book.getExtension(), '.pdf')
        self.assertRaises(self.book.importFile)

    def tearDown(self):
        self.book = ""


class TestAddressBookWithTextFile(unittest.TestCase):

    def setUp(self):
        mockConfig = MockConfig(constants.DEFAULT_TEXT_FILE)
        self.book = addressBook.AddressBook(mockConfig)

    def test_importContacts_as_txt(self):
        self.assertEquals(self.book.getExtension(), '.txt')
        self.assertEquals(self.book.contacts, None)
        self.book.importFile()
        self.assertEquals(len(self.book.contacts), 5)

    def tearDown(self):
        self.book = ''


class TestAddressBookWithJsonFile(unittest.TestCase):

    def setUp(self):
        mockConfig = MockConfig(constants.DEFAULT_JSON_FILE)
        self.book = addressBook.AddressBook(mockConfig)

    def test_importRaises(self):
        self.book.file_path = 'mock_file.pdf'
        self.assertRaises(self.book.importFile)

    def test_importContacts_as_json(self):
        self.assertEquals(self.book.getExtension(), '.json')
        self.assertEquals(self.book.contacts, None)
        self.book.importFile()
        self.assertEquals(len(self.book.contacts), 5)

    def test_exportContacts_as_json(self):
        self.book.importFile()
        self.book.exportFile()

    def tearDown(self):
        self.book = ''
