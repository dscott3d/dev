"""
Constants for the Tech Test.
"""

import os
import pkg_resources

DEFAULT_TEXT_FILE = pkg_resources.resource_filename(__name__, os.path.join("sample_data", "manual_data.txt"))
BAD_TEXT_FILE = pkg_resources.resource_filename(__name__, os.path.join("sample_data", "bad_manual_data.txt"))
EXPORT_TEXT_FILE = "exported_data.txt"

DEFAULT_JSON_FILE = pkg_resources.resource_filename(__name__, os.path.join("sample_data", "manual_data.json"))
BAD_JSON_FILE = pkg_resources.resource_filename(__name__, os.path.join("sample_data", "bad_manual_data.json"))
EXPORT_JSON_FILE = "exported_data.json"


def getExtension(file_path):
    return os.path.splitext(file_path)[1]
