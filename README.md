# Pytest Learning Project

A practical Python project created to learn and practice **pytest**, **unit testing**, **test fixtures**, **mocking**, **markers**, **test coverage**, **pytest configuration**, and **CI/CD with GitHub Actions**.

## 🛠️ Technologies Used

* Python 3.12
* pytest
* pytest-cov
* uv
* Git
* GitHub Actions
* Linux / Ubuntu

## 📚 Topics Covered

### 1. Unit Testing

* What is software testing?
* What is a unit?
* What is a unit test?
* Manual vs automated testing
* Unit testing vs integration testing
* Assertions

### 2. Pytest

* Installing pytest
* Writing test functions
* Running tests
* Verbose and quiet modes
* Running specific test files
* Running specific test functions
* Selecting tests with `-k`

### 3. Fixtures

* What are fixtures?
* Creating fixtures
* Using fixtures in tests
* Fixture scope
* `conftest.py`

### 4. Mocking

* Why mocking is needed
* `unittest.mock`
* `Mock`
* `patch`
* Mocking external services
* Mocking databases and APIs

### 5. Markers

* Built-in pytest markers
* Custom markers
* Running tests using markers

Example:

```bash
uv run python -m pytest -m calculator -v
```

### 6. Test Coverage

* What is test coverage?
* Installing `pytest-cov`
* Checking coverage
* Understanding `Stmts`, `Miss`, and `Cover`
* Finding missing coverage lines

Example:

```bash
uv run python -m pytest --cov
```

### 7. Pytest Configuration

Pytest configuration is maintained in `pyproject.toml`.

Example:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v"
markers = [
    "calculator: tests related to calculator functionality"
]
```

### 8. CI/CD

A local CI-style workflow was created using a shell script:

```bash
./run_ci.sh
```

The project also includes a GitHub Actions workflow that:

1. Checks out the repository
2. Sets up Python
3. Installs uv
4. Installs dependencies
5. Runs pytest

Workflow file:

```text
.github/workflows/python.yml
```

## 📁 Project Structure

```text
pytest-learning/
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── tests/
│   ├── ...
│
├── calculator.py
├── api_service.py
├── config.py
├── database_service.py
├── main.py
├── service.py
├── user_service.py
│
├── run_ci.sh
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

## 🚀 Setup

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd pytest-learning
```

Install/synchronize dependencies using uv:

```bash
uv sync
```

## 🧪 Running Tests

Run all tests:

```bash
uv run python -m pytest
```

Run tests in verbose mode:

```bash
uv run python -m pytest -v
```

Run a specific test file:

```bash
uv run python -m pytest tests/test_calculator.py
```

Run a specific test:

```bash
uv run python -m pytest tests/test_calculator.py::test_add -v
```

Run tests matching a keyword:

```bash
uv run python -m pytest -k add -v
```

Run tests using a marker:

```bash
uv run python -m pytest -m calculator -v
```

## 📊 Test Coverage

Run pytest with coverage:

```bash
uv run python -m pytest --cov
```

Show missing coverage lines:

```bash
uv run python -m pytest --cov --cov-report=term-missing
```

## 🔄 Local CI Workflow

The project contains a simple local CI script:

```bash
./run_ci.sh
```

It performs:

```text
Install dependencies
        ↓
    Run tests
        ↓
 Check exit status
        ↓
Pass → CI successful
Fail → CI failed
```

## ⚙️ GitHub Actions CI

The GitHub Actions workflow is located at:

```text
.github/workflows/python.yml
```

Whenever code is pushed to GitHub, the workflow automatically runs the test suite.

```text
Git Push
   ↓
GitHub Actions
   ↓
Checkout Code
   ↓
Setup Python
   ↓
Install uv
   ↓
uv sync
   ↓
Run pytest
   ↓
Tests Pass / Fail
```

## 🎯 Goal

The goal of this project is to build a strong practical understanding of **Python testing with pytest** and learn how automated testing fits into a real software development workflow using **CI/CD**.

## 👩‍💻 Author

**Shweta Boraganve**

Python | Pytest | SQL | Git | Linux 