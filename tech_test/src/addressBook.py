"""
Module to; import, store and export contact information.
"""

import os
import contactsImporter
import contactsExporter


class AddressBook(object):

    def __init__(self, config_args):
        self.file_path = config_args.input_file
        self.output_file = config_args.output_file
        self.contacts = None

    def getExtension(self):
        return os.path.splitext(self.file_path)[1]

    def importFile(self):
        info = contactsImporter.getImporter(self.file_path)
        info.readFile()
        info.parseInfo()
        self.contacts = info.contacts

    def exportFile(self):
        exported = contactsExporter.getExporter(self.output_file)
        exported.contacts = self.contacts
        exported.exportFile()
