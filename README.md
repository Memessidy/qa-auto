# QA-AUTO course project

My coursework project. It contains:
- UI tests (web pages tests): Proton mail interface, Rozetka, Amazon, Github
- Also protonmail creating tests using playwright
- Simple database queries tests
- Github REST API tests

## Requirements list
```
selenium==4.18.0
pytest==8.0.1
requests==2.31.0
webdriver-manager==4.0.1
Faker==23.2.1
pytest-playwright

To install you can type:
pip install -r requirements.txt
```
If you want to use playwright you should to install the required browsers:
```
playwright install
```

## All test are marked and you can run the required group of tests:
- pytest -m api
- pytest -m database
- pytest -m ui
- pytest -m http
- pytest -m ui_playwright
