 Page Content:
 1. How Pytest Works
 2. How to get Started with Pytest 
 3. TDD Best Practices
 4. official Docs

1.------------------- HOW PYTEST WORKS --------------------------

# What is pytest?
pytest is a testing framework for Python that allows you to write and run tests in a simple and expressive way.
used for unit tests, implementation tests, and End-to-end Tests (system Tests) 

# How does pytest work
pytest uses a combination of introspection, automatic test discovery, and test execution to simplify the testing process.
Test discovery: pytest automatically discovers and collects tests by looking for files that start with test_ or end with _test and searching for test functions or classes within them.
Test execution: pytest runs the discovered tests using its test runner, which provides a rich set of features for running and reporting test results.
Assertions: pytest provides a powerful assertion mechanism that allows you to make statements about expected behavior in your tests. It automatically captures and presents detailed information when assertions fail.

# Why use pytest?
Simplicity: pytest aims to provide a simple and intuitive way to write tests. Its minimalist syntax and powerful features make test code clean and easy to read.
Flexibility: pytest supports a wide range of testing scenarios, from simple unit tests to complex functional and integration tests. It allows you to customize test collection and execution using plugins and fixtures.
Extensibility: pytest is highly extensible through a plugin architecture. You can leverage existing plugins or create your own to enhance the functionality and adapt pytest to your specific needs.
Integration: pytest integrates well with other tools and frameworks commonly used in the Python ecosystem, such as coverage tools, continuous integration systems, and test runners like tox and Jenkins.

Pytest provides an efficient and developer-friendly approach to testing in Python, making it a popular choice for testing Python applications of all sizes and complexities.
 
 

2.--------------------HOW TO GET STARTED WITH PYTEST---------------------------

1. Install pytest: Make sure pytest is installed in your Python environment. You can install it using pip by running the command pip install pytest in your terminal.

2. Create a test file: Create a new Python file in your project directory and name it starting with test_ or ending with _test. For example, test_math.py.

3. Write your tests: Inside the test file, write your test functions using the pytest framework. Test functions should start with test_ and can include assertions to validate the behavior of your code.

4. Configure the test runner: In Visual Studio Code, open the Command Palette by pressing Ctrl+Shift+P (or Cmd+Shift+P on macOS) and search for "Python: Configure Tests". Select "pytest" as the test framework.

5. Run the tests: To run the tests, open the test file in the editor or navigate to the file in the Explorer sidebar. Then, use the "Run Test" button that appears above the test function or right-click and select "Run Test" from the context menu. Alternatively, you can run all tests in the project by opening the Command Palette and running the command "Python: Run All Tests".

6. View test results: After running the tests, the test results will be displayed in the "Test Explorer" panel in Visual Studio Code. You can see the status of each test (passed, failed, or skipped) and access detailed information about the test runs.

7. Customize your tests: You can customize your test runs by adding test configurations in the pytest.ini or pyproject.toml files. These files allow you to specify additional options and settings for pytest.

That's it! You can now write and run tests using pytest in Visual Studio Code. Remember to follow the naming conventions for test files and functions, and pytest will automatically discover and execute your tests.


3.-------------------BEST PRACTICES TO REMEMBER WHEN TDD'ing----------------------
# - remember naming conventions 
# - test first code later 
# - Order of tests matter, from a security perspective
# - too many unit tests can slow down your code- use more implementation testing 
# - test edge scenarios
# - Always Be Testing, especially with CI/CD (github scenario)
# - test after every change, no matter how small 


-------------------------------------Documentation: ------------------------------
Official documentation: https://docs.pytest.org/en/7.3.x/getting-started.html#create-your-first-test
