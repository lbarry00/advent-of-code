# Advent of Code Solutions

It's my annual tradition of saying, "This will be the year" and then not bothering to complete all of the problems.

This is a repo with my solutions and driver code.

## About

### `driver.py`
Driver code for reading problem input, running solution code on it, and outputting the results. Modify the `DAY` and `YEAR` constants to adjust which solution to run.

### `generate.py`
Script for generating folder and files for a day's solution. The folder structure simply looks like this:
```
YEAR/
├── DAY/
│   ├── input.txt
│   └── solution.py
└── DAY/
    ├── input.txt
    └── solution.py
    ...
```

> **_NOTE:_**  Both `driver.py` and `generate.py` have VS Code Launch Configurations set up.

### `solution-template.py`
Template code for python solution. The generate script copies this into each day's `solution.py` file. (Yes, I have automated writing 5 lines of code.) This does not need to be modified or really have anything done to it, as the generate script does everything. 