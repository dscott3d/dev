"""
Unittests for the Contact Exporters.
"""

import os
import unittest

from src import contactsExporter
from src import constants
from src import errors


class TestGetImporter(unittest.TestCase):

    def test_getTextExporter(self):
        self.assertEquals(type(contactsExporter.getExporter('mock.txt')),
                          type(contactsExporter.TextExporter('mock.txt')))

    def test_getJsonExporter(self):
        self.assertEquals(type(contactsExporter.getExporter('mock.json')),
                          type(contactsExporter.JsonExporter('mock.json')))

    def test_getExporterError(self):
        self.assertRaises(errors.EmptyBookError, contactsExporter.getExporter, 'mock.pdf')


class TestBaseExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = contactsExporter.BaseExporter(constants.EXPORT_JSON_FILE)

    def test_exportFile(self):
        self.assertRaises(self.exporter.exportFile())

    def tearDown(self):
        self.exporter = ""


class TestTextExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = contactsExporter.TextExporter(constants.EXPORT_TEXT_FILE)
        self.exporter.contacts = getMockContacts()

    def test_exportFile(self):
        self.exporter.exportFile()
        exported_data = readTempTestFile(constants.EXPORT_TEXT_FILE)
        self.assertEquals(len(exported_data), 2)

    def tearDown(self):
        os.remove(self.exporter.file_path)
        self.exporter = ""


class TestJsonExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = contactsExporter.JsonExporter(constants.EXPORT_JSON_FILE)
        self.exporter.contacts = getMockContacts()

    def test_exportFile(self):
        self.exporter.exportFile()

    def tearDown(self):
        os.remove(self.exporter.file_path)
        self.exporter = ""


def getMockContacts():
    contacts = {'testContact1': {'name': "Test Contact 1",
                                 'address': "Home 1",
                                 'phone': "555-1111"},
                'testContact2': {'name': "Test Contact 2",
                                 'address': "Home 2",
                                 'phone': "555-2222"}}
    return contacts


def readTempTestFile(exportedFile):
    exported_data = []
    with open(exportedFile, 'r') as fileOpen:
        for line in fileOpen:
            exported_data.append(line)
    return exported_data
