# SHIRT Tests

This directory contains tests for the SHIRT command-line tool. The tests cover various functionalities of the tool, such as basic renaming, recursive renaming, inverting the match, and dry-run functionality.

## Running the tests

We recommend using `pytest` to run the tests. To install `pytest`, you can use the following command:

```bash
pip install pytest
```

Once `pytest` is installed, navigate to the top-level directory of the repository and run the following command to execute the tests:

```bash
pytest tests/
```

`pytest` will automatically discover and run the tests in the `tests` directory.

If you want to run a specific test file, you can specify the file path in the command:

```bash
pytest tests/test_shirt.py
```

## Adding new tests

To add new tests, create a new test file in the `tests` directory with a name starting with `test_` and ending with `.py`. For example, you can create a file named `test_new_feature.py`. Inside the test file, write your test functions with names starting with `test_`. The test runner will automatically discover and execute them.

Make sure to import the necessary modules and functions from the main script to use in your tests.
