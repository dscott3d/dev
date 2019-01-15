**Daniel Scott's Tech Test**

This package contains a commandline module to import and export contact details. The two currently supported formats for import/export are `.txt` and `.json`.

To run the code (with help):<br>
`python commandline.py --help`

By default the code will import the sample text file, contained, in the "src/sample_data" folder.

To import your own data, run the following:<br>
`python commandline.py -i <path to your file>`

By default, the tool with export the processed data to the local directory as:
`exported_data.txt`

This can be overridden using:<br>
`python commandline.py -i <path to your file> -o <chosen exported file path>`

To run the tests, use the following:<br>
`python -m unittest discover`