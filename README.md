### API Test Framework
Contains API automation tests and supporting code for testing the Data Quality product.

### Setup

1. Clone the repository:
```commandline
git clone git@github.com:collibra/dq-test-automation.git
```
2. Setup:

- BEST PRACTICE: Use the Virtual Environments for running your tests:
Venv [docs](https://docs.python.org/3/tutorial/venv.html) 

Once virtual environment is launched, install the dependencies:
```commandline
cd path/dq-test-automation

pip install -r requirements.txt
```
3. Running the tests:

- From the root of the project, issue the command:
```commandline
pytest --base_url=<url> --iss=validation
```
### Test Reports

- The framework uses allure for reporting
- While running the job, give the report output folder directory path

For Example:
```commandline
pytest --base_url=<url> --iss=validation --alluredir=allure-results
```
Once the run is complete, simply run:
```commandline
allure serve allure-results
```
For more information about allure please refer [here](https://docs.qameta.io/allure/)

### Language/Frameworks:

- [Python](https://www.python.org/) - Programming Language
- [Pytest](https://docs.pytest.org/en/7.3.x/) - Testing Framework
- [Requests](https://pypi.org/project/requests/) - HTTP Library for Python
- [Assertpy](https://github.com/assertpy/assertpy) - Assertions library for unit testing in Python
- [Allure Pytest](https://pypi.org/project/allure-pytest/) - Reporting Library

### Recommended IDE:

- [PyCharm](https://www.jetbrains.com/pycharm/) - The Python IDE
- [Vscode](https://code.visualstudio.com/) - Source code editor
