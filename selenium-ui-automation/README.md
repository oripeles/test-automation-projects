Selenium UI Automation – Demo E-Commerce Project

This project is a UI test automation framework built with Python, Selenium, and Pytest, targeting a demo e-commerce website.
The goal of this project is to demonstrate clean automation architecture, Page Object Model, Docker integration, CI/CD (GitHub Actions), environment variables, and Allure reporting.

🔧 Tech Stack

Language: Python 3.11

Framework: Selenium WebDriver 4

Test Runner: Pytest (+ pytest-ordering)

Reporting: Allure Framework

Driver Management: webdriver-manager

Containerization: Docker (Headless Chrome)

CI/CD: GitHub Actions (Linux runners + Docker jobs)

📌 Key Features

Full UI automation for common e-commerce flows:

New user registration

Login (valid & invalid)

Logout flow

Product search

Category browsing

Product detail validation

Add / remove products from cart

Quantity verification

Newsletter subscription

Test Cases page validation

Page Object Model (clean and maintainable)

Environment-based password handling (no secrets in JSON)

Allure reporting for full test visualization

Support for local execution and Docker execution

Full CI/CD integration

selenium-ui-automation/
├── pages/                 
├── tests/                
├── data/                 
├── utilities/             
├── screenshots/           
├── conftest.py            
├── requirements.txt      
├── Dockerfile             
└── README.md            

▶️ Running the Tests Locally (No Docker)
1. Create and activate a virtual environment
cd selenium-ui-automation
python3 -m venv .venv
source .venv/bin/activate
2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
3. Set the password environment variable
The existing user password is not stored in JSON.
export USER_PASSWORD="YourLocalPassword"
4. Run the test suite
pytest --alluredir=allure-results
5. Generate the Allure report
allure serve allure-results

🐳 Running Tests with Docker
1. Build the Docker image
docker build -t selenium-tests .
2. Run tests inside the Docker container
docker run --rm \
  -e USER_PASSWORD="YourLocalPassword" \
  -v $(pwd)/allure-results:/app/allure-results \
  selenium-tests
3. View the Allure report
allure serve allure-results

⚙️ CI/CD – GitHub Actions

This project includes a GitHub Actions pipeline that runs the Selenium UI tests **inside Docker** on every push to the `main` branch.

The workflow:

- Checks out the repository  
- Builds a Docker image from the `selenium-ui-automation` Dockerfile  
- Runs the tests inside a headless Chrome container  
- Maps the `allure-results` directory from the container back to the GitHub runner  
- Uploads the Allure results as a workflow artifact (`allure-results-docker`)

Workflow file:
.github/workflows/tests.yml

Builds the Docker image defined in Dockerfile

Runs the tests inside Docker with headless Chrome

Extracts Allure results from inside the container

Uploads them as separate artifacts (allure-results-docker)

Workflow file:
.github/workflows/tests.yml

🔐 Environment Variables

Sensitive data like the existing user’s password is injected via:

os.getenv("USER_PASSWORD") in Python

GitHub Secrets in CI

Local shell environment variable when running locally

This keeps the framework secure and production-ready.

