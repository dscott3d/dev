"""
Unittests for the Commandline module.
"""

import unittest

from src import commandline
from src import constants

TEST_ARGS = ['--input_file', constants.DEFAULT_TEXT_FILE]


class TestCommandline(unittest.TestCase):

    def setUp(self):
        self.parser = commandline.parse_args(TEST_ARGS)

    def test_parse_args_file(self):
        self.assertEquals(self.parser.input_file, constants.DEFAULT_TEXT_FILE)

    def test_getContactDetails(self):
        addressBook = commandline.getContactDetails(TEST_ARGS)
        self.assertTrue('Text File' in addressBook.contacts.keys())

    def tearDown(self):
        self.parser = ""
