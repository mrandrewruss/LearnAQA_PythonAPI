## REST API test automation in Python 🐍
[//]: # (Автоматизация тестирования REST API на Python )


- **Simple API requests** ⚙️
  - [x] Parsing JSON
  - [x] Headers
  - [x] Cookie
  - [x] Status code 
  - [x] Redirects (300 & 301)


- **Pytest** 🛠
  - [x] Pytest and simple tests
  - [x] Parameterized test
  - [x] Positive/negative authorization tests
  - [x] The setup() function in Pytest
  - [x] BaseCase
  - [x] Assertions


- **Creation of a framework & running in Docker** 🐳
  - [x] Create an existing user
  - [x] Creating a new user
  - [x] User View
  - [x] User editing
  - [x] Transferring a request to a method
  - [x] Replacing Methods
  - [x] Logging
  - [x] Allure (add: @allure.epic + @allure.description + with allure.step("abc"))
  - [ ] Environment
  - [ ] Running Tests in Docker


---
`pip3 install -r requirements.txt` -> _install packages from requirements file_

#### Pytest
`python3 -m pytest tests` -> _running tests (all)_

#### Allure
`python3 -m pytest --alluredir=test_results/ tests/test_user_auth.py` -> _running test with allure_

`allure serve test_results/` -> _allure report generation_


