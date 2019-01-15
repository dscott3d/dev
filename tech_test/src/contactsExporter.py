"""
Module to import a variety of supported formats.
"""

import json
import constants
import errors


def getSupportedExportFormats():
    formats = []
    for cls in BaseExporter.__subclasses__():
        formats.append(cls.ext)
    return formats


def getExporter(file_path):
    """
    Export Factory to return the relevant Exporter, or raise an error if an unsupported file is supplied.
    """
    _class = None

    for cls in BaseExporter.__subclasses__():
        if cls.ext == constants.getExtension(file_path):
            _class = cls(file_path)

    if _class:
        return _class
    else:
        raise errors.EmptyBookError("Address book is empty! Unsupported file extension: %s"
                                    % constants.getExtension(file_path))


class BaseExporter(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.ext = None
        self.contacts = {}

    def exportFile(self):
        return NotImplemented


class TextExporter(BaseExporter):

    ext = '.txt'

    def exportFile(self):
        file_open = open(self.file_path, "w")
        for each in self.contacts:
            e = self.contacts[each]
            file_open.write("%s,%s,%s\n" % (e['name'], e['address'], e['phone']))
        file_open.close()


class JsonExporter(BaseExporter):

    ext = '.json'

    def exportFile(self):
        with open(self.file_path, "w") as outfile:
            json.dump(self.contacts, outfile)
