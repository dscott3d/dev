"""
Module to import a variety of supported formats.
"""

import json
import errors
import constants


def getSupportedImportFormats():
    formats = []
    for cls in BaseImporter.__subclasses__():
        formats.append(cls.ext)
    return formats


def getImporter(file_path):
    """
    Import Factory to return the relevant Importer, or raise an error if an unsupported file is supplied.
    """
    _class = None

    for cls in BaseImporter.__subclasses__():
        if cls.ext == constants.getExtension(file_path):
            _class = cls(file_path)

    if _class:
        return _class
    else:
        raise errors.EmptyBookError("Address book is empty! Unsupported file extension: %s"
                                    % constants.getExtension(file_path))


class BaseImporter(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.ext = None
        self.info = []
        self.contacts = {}

    def readFile(self):
        return NotImplemented

    def parseInfo(self):
        return NotImplemented

    def isValidEntry(self):
        return NotImplemented


class TextImporter(BaseImporter):

    ext = '.txt'

    def readFile(self):
        with open(self.file_path, "r") as fileOpen:
            for line in fileOpen:
                self.info.append(line.split('\n')[0])

    def parseInfo(self):

        for each in self.info[1:]:
            c = {}
            info = each.split(',')
            if self.isValidEntry(info):
                c['name'] = info[0]
                c['address'] = info[1]
                c['phone'] = info[2]
                self.contacts[c['name']] = c
            else:
                raise errors.ContactError("Expected information containing: Name, Address, Phone Number")

    def isValidEntry(self, info):
        return True if len(info) == 3 else False


class JsonImporter(BaseImporter):

    ext = '.json'

    def readFile(self):
        with open(self.file_path) as json_file:
            self.info = json.load(json_file)

    def parseInfo(self):
        for each in self.info:
            if self.isValidEntry(each):
                contact = {'name': self.info[each]['name'],
                           'address': self.info[each]['address'],
                           'phone': self.info[each]['phone']}
                self.contacts[each] = contact
            else:
                raise errors.ContactError("Expected information containing: Name, Address, Phone Number")

    def isValidEntry(self, entry):
        if 'name' in self.info[entry] and 'address' in self.info[entry] and 'phone' in self.info[entry]:
            return True
        else:
            return False
