"""
Commandline entry point to the AL Tech Test

By: Daniel Scott
dscott3d@sketchdigital.com.au
"""

import argparse
import sys

import addressBook
import constants
import contactsImporter
import contactsExporter


def parse_args(args, prog_version='1.0', prog_usage='', misc_opts=None):
    parser = argparse.ArgumentParser(description='Commandline tool to read, store and display contact details. The currently'
                                                 'supported formats are:\n- import formats: %s\n-export formats: %s' %
                                                 (contactsImporter.getSupportedImportFormats(),
                                                  contactsExporter.getSupportedExportFormats()))
    parser.add_argument('-i',
                        '--input_file',
                        default=constants.DEFAULT_TEXT_FILE,
                        help="The input file, which should containing comma separated data, eg. Name, Address, Phone" \
                             " on each line, for each entry.")
    parser.add_argument('-o',
                        '--output_file',
                        default=constants.EXPORT_TEXT_FILE,
                        help="The output file to export the data.")
    return parser.parse_args(args)


def getContactDetails(args):
    book = addressBook.AddressBook(parse_args(args))
    book.importFile()
    book.exportFile()
    return book


if __name__ == '__main__':
    book = getContactDetails(sys.argv[1:])
