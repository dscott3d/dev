**Daniel Scott's Tech Test**

This package contains a commandline module to import and export contact details. The two currently supported formats for import/export are `.txt` and `.json`.

To run the code (with help):<br>
`python src/commandline.py --help`

By default the code will import the sample text file, contained, in the "src/sample_data" folder.

To import your own data, run the following:<br>
`python src/commandline.py -i <path to your file>`

By default, the tool with export the processed data to the local directory as:
`exported_data.txt`

This can be overridden using:<br>
`python src/commandline.py -i <path to your file> -o <chosen exported file path>`

The tool will manage the data, and can convert to any format, eg:<br>
- txt > txt<br>
- txt > json<br>
- json > txt<br>
- json > json<br>

The sample data shows good and bad examples. The text files should contain one entry per line, with comma separation. No header line needed. The Json file should contain a name, address and phone for each entry.

To run the tests, use the following:<br>
`python -m unittest discover`