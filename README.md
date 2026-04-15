# E-commerce Playwright Automation
E2E automation test project for e-commerce website, built with Python + Playwright + pytest, integrated with GitHub Actions for continuous testing and HTML report generation.

## 📌 Setup Instructions
### 1. Prerequisites
Python 3.9+ installed
Git (optional, for version control)

### 2. Install Dependencies
Install required Python packages
pip install pytest pytest-html playwright
Install Playwright browser dependencies
playwright install --with-deps chromium

### 3. Run Tests
Run all tests with verbose output
pytest -v
Run tests and generate HTML test report
pytest --html=reports/report.html --self-contained-html -v
The report will be saved to reports/report.html, which can be opened directly in any browser.

### 4. GitHub Actions CI/CD
This project is integrated with GitHub Actions. The test workflow will automatically trigger on every push or pull request to the main branch:
Automatically installs dependencies and Playwright browsers
Executes all E2E test cases
Generates and uploads the HTML test report as an artifact
Retention period for test reports: 30 days
You can download the report from the Artifacts section in the GitHub Actions workflow run page.

## 📌 What's Covered
This test suite covers core end-to-end business flows of the e-commerce platform:
User Authentication: Login/logout functionality, invalid credential validation
Product Browsing: Product listing, category filtering, product detail page validation
Shopping Cart Operations: Add/remove items (in-stock & out-of-stock scenarios), cart quantity adjustment
Checkout Flow: Cart review, checkout process, order confirmation
UI & UX Validation: Cookie consent banner handling, page navigation, element visibility checks

## 📌 Known Limitations
Selector Dependency: Tests rely on static UI element selectors. Any changes to the website's frontend structure (e.g., class names, element IDs) may cause test failures.
Environment Dependency: Tests are designed for a specific test environment. Changes to test data, product availability, or environment configuration may impact test results.
Execution Mode: Currently configured for sequential execution; parallel test execution is not enabled in CI.
Wait Strategy: Some test steps use fixed time waits to handle page loading, which may lead to flakiness in unstable network conditions.
Browser Support: Currently only Chromium is configured for testing; cross-browser testing (Firefox, Safari) is not implemented.

## 📁 Project Structure
ecommerce-playwright-automation/
├── .github/workflows/ # GitHub Actions CI configuration
├── pages/ # Page Object Model (POM) classes for UI elements
├── tests/ # Test case files
├── config/ # Configuration files (e.g., test URLs, credentials)
├── reports/ # Generated HTML test reports (git-ignored)
├── requirements.txt # Project dependencies
├── pytest.ini # pytest configuration
└── README.md # Project documentation
