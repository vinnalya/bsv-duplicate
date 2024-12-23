# Requirements Specification

This document specifies the requirements of the **BibTeX Duplicate Detector** system.

## Functional Requirements

The following requirement, specified in the use case format, is in scope of the system.

| UC1 | Detect Duplicates |
|---|---|
| Actors | Researcher |
| Preconditions | The researcher has a bibliography in BibTeX format |
| Main Success Scenario | 1. When the researcher uploads a bibliography in the correct file format, the system processes the list and prompts the researcher what to do next. |
| | 2. When the researcher selects "Show duplicates", the system found duplicates, and the number of duplicates is less than 10, then the system prints the keys of the dupliates on the screen. |
| Postconditions | The researcher sees all identified duplicates. |
| Extensions | 1b. If the uploaded bibliography is not in the correct file format, the system displays an error. |
| | 2.b If the researcher selects "Show duplicates" and the system did not find any duplicates, the system notifies the researcher that the bibliography is free of duplicates. |
| | 2.c If the researcher selects "Show duplicates", the system foudn duplicates, and the number of duplicates is 10 or more, then the system downloads both a list of the duplicates and a version of the bibliography without any duplicates. |

## Non-functional Requirements

Any implementation of the system shall adhere to the following quality requirements:

1. The system shall be easily maintainable.
2. The system shall be reliable in the detection of duplicates.
3. The system shall be easy to integrate into other systems (e.g., Overleaf).
