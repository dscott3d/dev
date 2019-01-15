"""
Unittests for the Contact Importers.
"""

import unittest

from src import contactsImporter
from src import constants
from src import errors


class TestGetExtension(unittest.TestCase):

    def test_getExtension(self):
        self.assertEquals(constants.getExtension('mock.xyz'), '.xyz')


class TestGetImporter(unittest.TestCase):

    def test_getTextImporter(self):
        self.assertEquals(type(contactsImporter.getImporter('mock.txt')),
                          type(contactsImporter.TextImporter('mock.txt')))

    def test_getJsonImporter(self):
        self.assertEquals(type(contactsImporter.getImporter('mock.json')),
                          type(contactsImporter.JsonImporter('mock.json')))

    def test_getImporterError(self):
        self.assertRaises(errors.EmptyBookError, contactsImporter.getImporter, 'mock.pdf')


class TestBaseImporter(unittest.TestCase):

    def setUp(self):
        self.importer = contactsImporter.BaseImporter("mock.pdf")

    def test_readFile(self):
        self.assertRaises(self.importer.readFile())

    def test_parseInfo(self):
        self.assertRaises(self.importer.parseInfo())

    def test_isValidEntry(self):
        self.assertRaises(self.importer.isValidEntry())

    def tearDown(self):
        self.importer = ""


class TestTextImporter(unittest.TestCase):

    def setUp(self):
        self.importer = contactsImporter.TextImporter(constants.DEFAULT_TEXT_FILE)

    def test_text_importer(self):
        self.assertEquals(len(self.importer.info), 0)
        self.importer.readFile()
        self.assertEquals(len(self.importer.info), 6)

    def test_parseInfo(self):
        self.importer.readFile()
        self.importer.parseInfo()
        self.assertEquals(len(self.importer.contacts), 5)
        self.assertEquals(self.importer.contacts['Bruce Wayne']['address'], 'Wayne Manor')

    def test_raisesError(self):
        bad_file = constants.BAD_TEXT_FILE
        self.importer = contactsImporter.TextImporter(bad_file)
        self.importer.readFile()
        self.assertRaises(errors.ContactError, self.importer.parseInfo)

    def tearDown(self):
        self.importer = ""


class TestJsonImporter(unittest.TestCase):

    def setUp(self):
        self.importer = contactsImporter.JsonImporter(constants.DEFAULT_JSON_FILE)

    def test_text_importer(self):
        self.assertEquals(len(self.importer.info), 0)
        self.importer.readFile()
        self.assertEquals(len(self.importer.info), 5)

    def test_parseInfo(self):
        self.importer.readFile()
        self.importer.parseInfo()
        self.assertEquals(len(self.importer.contacts), 5)
        self.assertEquals(self.importer.contacts['Bruce Wayne']['address'], 'Wayne Manor')

    def test_raisesError(self):
        bad_file = constants.BAD_JSON_FILE
        self.importer = contactsImporter.JsonImporter(bad_file)
        self.importer.readFile()
        self.assertRaises(errors.ContactError, self.importer.parseInfo)

    def tearDown(self):
        self.importer = ""
