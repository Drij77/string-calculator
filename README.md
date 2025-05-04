# String Calculator

A Python implementation of the String Calculator kata.

## Project Structure

```
string_calculator/
├── string_calculator.py    # Main implementation
└── tests/
    └── test_string_calculator.py  # Test suite
```

## Requirements

- Python 3.6 or higher
- pytest (for running tests)

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install pytest
```

## Running Tests

To run the test suite:
```bash
pytest
```

## Features

The string calculator can:
- Handle empty strings
- Handle single numbers
- Handle multiple numbers separated by commas
- Handle newlines as delimiters
- Support custom delimiters

