# kmg_csv2json

This is a Python script to ease batch creation of module entries for [kosmodulargrid](https://www.kosmodulargrid.com/), by converting a CSV file and generating the needed UUIDs.

To use: Create a CSV file with these fields: **id, makerId, function, name, description, width, type, link, imageLink**. (Most easily done by making a spreadsheet and exporting as CSV. For a sample sheet see [here](https://docs.google.com/spreadsheets/d/1q_zL7uwcyrEbk5R7C60tEQWUtUBpQ3iB7ykcuLSns50/edit?usp=sharing).) Run script as:

```
kmg.py <csvfile> [<makerId>]
```

JSON conversion is output to stdout.

In function and type columns, comma separated values will become list entries. 

If the 'makerId' field is empty, a default value is filled in. At startup the default value is the second command line argument, if present. If not, a new UUID will be generated for the default. If the 'makerId' field is nonempty (and its value is not 'makerId'), that value will be used for that entry and will become the default for subsequent entries. Typically the way to proceed would be: Leave 2nd argument off and 'makerId' field blank the first time you run the script, then put the generated UUID in the 'makerId' field for the first row or 2nd command line argument on subsequent runs.

Lines with nonempty 'id' field will generate no output (so you can safely include a header line, or lines that describe modules already listed if they have an id entered).

Lines with empty 'id' field will generate output, and a new UUID will be generated for the 'id' field. 
