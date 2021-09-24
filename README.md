#kmg_csv2json

This is a Python script to ease batch creation of module entries for [kosmodulargrid](https://www.kosmodulargrid.com/), by converting a CSV file and generating the needed UUIDs.

To use: Create a CSV file with these fields: **id, makerId, function, name, description, width, type, link, imageLink**. (Most easily done by making a spreadsheet and exporting as CSV. For a sample sheet see [here](https://docs.google.com/spreadsheets/d/1q_zL7uwcyrEbk5R7C60tEQWUtUBpQ3iB7ykcuLSns50/edit?usp=sharing).) Run script as:

```
kmg.py <csvfile> [<makerId>]
```

JSON conversion is output to stdout.

In function and type columns, comma separated values will become list entries. 

Lines with nonempty 'id' will be ignored (so you can safely include a header line, or lines that describe modules already listed if they have an id entered).

Lines with empty 'id' will be included in the output, and a new UUID will be generated for the 'id' field.

If 'makerId' is empty, a default value is filled in. At startup the default value is the second command line argument, if present. If not, a new UUID will be generated for the default. If 'makerId' is nonempty, that value will be used for that entry and will become the default for subsequent entries. Typically the way to proceed would be: Leave 2nd argument off and 'makerId' column blank the first time you run the script, then put the generated UUID in the 'makerId' field for the first row or 2nd command line argument on subsequent runs.
