# Detection of Duplicates in Bibtex References

[![GitHub](https://img.shields.io/github/license/bth-dipt-teaching/bsv-duplicate)](./LICENSE)

This repository contains a toy system which detects duplicate entries from `.bib` files which contain a list of references to scientific articles.

> [!CAUTION]
> This is a toy system containing **seeded defects**! Do not use this code for production purposes.

## Repository Structure

The repository contains the following files.

```
├── data : directory containing data
│   └── references.bib : an exemplary data file in .bibtex format
├── doc : directory containing documentation files
│   ├── context-specification.md : context of the system, describing why the system needs to be realized
│   ├── requirements-specification.md : requirements of the system, describing what needs to be realized
│   └── system-specification.md : specification of the system, describing how the system will be realized
├── src : directory containing all source code
│   ├── util: supporting files for the main file
│   │   ├── detector.py : script implementing the duplicate detection
│   │   └── parser.py : script for parsing the raw text file into a list of Article objects
│   └── main.py: main file executing the functionality
├── test : directory containing all test files
│   ├── demo/test_demo.py : meaningless passing test case 
│   └── unit : directory for the unit tests of the system
│       └── test_detect_duplicates.py : file to create test cases for the detect_duplicates.py script
├── pytest.ini : configuration of the testing environment
└── requirements.txt : list of required libraries
```

## Usage

To familiarize yourself with the system, read the [context specification](./doc/context-specification.md), [requirements specification](./doc/requirements-specification.md), and [system specification](./doc/system-specification.md) in this order.

To execute the system in its current form, make sure that you have [Python 3.10](https://www.python.org/downloads/release/python-3100/) available on your system.
Then, execute the following steps:

1. Install all required packages via `pip install -r requirements.txt`.
2. Execute the following command from the *src/* directory: `python .\main.py`.

You should see a list of bibtex article keys in the console output.

## Testing

To run the test suite, execute the following command from the root directory:

```
pytest -m <marker>
```

Replace `<marker>` with any of the available markers from [pytest.ini](pytest.ini).
Currently, using the marker `demo` will execute a simple, failing test case.
The real test cases to be developed in the [test_detect_duplicates.py](./test/unit/test_detect_duplicates.py) file shall be marked with `unit`.

> [!TIP]
> If you are unable to execute the test cases locally, make use of the GitHub action: push your code to your fork of the repository and inspect the output of the **Pytest** action.

## License

Copyright © 2024 by Julian Frattini. 
This work (source code) is available under the [MIT license](./LICENSE).
