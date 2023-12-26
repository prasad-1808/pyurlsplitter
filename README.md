# PYURLSPLITTER

# Overview
- PYURLSPLITTER is a Python tool designed for splitting a list of URLs provided in a text file.
- This tool generates various combinations of URLs and provides the output in an output.txt file.
- The output.txt file includes the overall URL list with duplicates removed.

# To Run the tool:
- Using GitHub:
  - git clone <https://github.com/prasad-1808/pyurlsplitter.git>
  - cd pyurlsplitter/pyurlsplitter
  - python urlsplitter.py -t <input.txt> -o <output.txt>
  - -t OR --target: Target input file
  - -o OR --output: Output file
 
- Using pip
    - pip install pyurlsplitter
    - Arguments:
        - -h | --help 
        - -t | --target <input.txt>
        - -o | --output <output.txt>
     - pyurlsplitter -t <input.txt> -o <output.txt>
     - pyurlsplitter -h
