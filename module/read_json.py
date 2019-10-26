#!/usr/local/bin/python3.7

# =========================================================================================
#
# NAME:           read_json.py
# DESCRIPTION:    Python module to read from json file and print
# AUTHOR:         Manish Sharma
# VERSION:        1.0
# CREATED:        Oct 16, 2019
#
# =========================================================================================

import json

with open('/tmp/version_info.json', 'r') as f:
    version_dict = json.load(f)

print(version_dict["java"]["version"])
