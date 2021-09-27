#!/usr/bin/python3

# CSV to JSON for kosmodulargrid, with UUID generation
# Rich Holmes, September 2021
# CC0 v1.0

import uuid
import csv
import json
from sys import argv
import re

# To use: Create a CSV file with these fields:
# id, makerId, function, name, description, width, type, link, imageLink
# (Most easily done by making a spreadsheet and exporting as CSV).
# Run script as:
#
# kmg.py <csvfile> [<makerId>]
#
# JSON conversion is output to stdout.
#
# In function and type columns, comma separated values will become
# list entries.
#
# Lines with nonempty 'id' will be ignored (so you can safely include
# a header line, or lines that describe modules already listed if they
# have an id entered).
#
# Lines with empty 'id' will be included in the output, and a new UUID
# will be generated for the 'id' field.
#
# If 'makerId' is empty, a default value is filled in. At startup the
# default value is the second command line argument, if present. If
# not, a new UUID will be generated for the default. If 'makerId' is
# nonempty, that value will be used for that entry and will become the
# default for subsequent entries. Typically the way to proceed would
# be: Leave 2nd argument off and 'makerId' column blank the first time
# you run the script, then put the generated UUID in the 'makerId'
# field for the first row or 2nd command line argument on subsequent
# runs.

def main():

    # 1st arg is filename
    # 2nd arg is default makerId, if present
    # else generate a new UUID for default makerId
    fn = argv[1]
    defmakerId = argv[2] if len(argv) == 3 else str(uuid.uuid4())

    # Fields must be present in this order in the CSV
    # Empty fields will default to empty string.
    fldn = ['id', 'makerId', 'function', 'name', 'description',
            'width', 'type', 'link', 'imageLink']

    # Process the file
    datalist = []
    with open (fn, 'r') as f:
        # Read CSV into dictionary
        freader = csv.DictReader (f, fieldnames=fldn, restval='')

        # Process lines
        for fi in freader:
            data = {key: fi[key] for key in fldn}

            # ignore header line, and if id is otherwise filled in we assume
            # it's already been listed
            # Otherwise generate a new UUID
            if data['id'] == '': 
                data['id'] = str(uuid.uuid4())
            else:
                continue

            # use default makerId if none supplied, otherwise make that
            # the new default
            if data['makerId'] == '':
                data['makerId'] = defmakerId
            else:
                defmakerId = data['makerId']

            # split 'function' and 'type' fields
            if data['function'] != '':
                data['function'] = re.split(',\s*', data['function'])
            else:
                data['function'] = []
            if data['type'] != '':
                data['type'] = re.split(',\s*', data['type'])
            else:
                data['type'] = []

            # width should be number
            if '.' in data['width']:
                data['width'] = float(data['width'])
            elif data['width'] != "":
                data['width'] = int(data['width'])

            datalist.append(data)
            
        # JSON to stdout
        print (json.dumps(datalist, indent=2))

if __name__ == '__main__':
    main()
