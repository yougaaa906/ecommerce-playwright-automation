# E-commerce Playwright Automation

E2E automation test project for e-commerce website, built with Python + Playwright + pytest, integrated with GitHub Actions for continuous testing and HTML report generation.

---

## Setup Instructions

### 1. Prerequisites
- Python 3.9+ installed
- Git (optional, for version control)

### 2. Install Dependencies
- pip install pytest pytest-html playwright
- playwright install --with-deps chromium

### 3. Run Tests
pytest -v

pytest --html=reports/report.html --self-contained-html -v

The report will be saved to reports/report.html, which can be opened directly in any browser.

### 4. GitHub Actions CI/CD
- This project is integrated with GitHub Actions. The test workflow will automatically trigger on every push or pull request to the main branch.
- You can download the report from the Artifacts section in the GitHub Actions workflow run page.

---

## What's Covered
- User Authentication: Login/logout functionality, invalid credential validation
- Product Browsing: Product listing, category filtering, product detail page validation
- Shopping Cart Operations: Add/remove items (in-stock & out-of-stock scenarios)
- Checkout Flow: Cart review, checkout process, order confirmation
- UI & UX Validation: Cookie consent banner handling, page navigation

---

## Known Limitations
1. Tests rely on static UI element selectors. Any changes to the website's frontend structure may cause test failures.
2. Tests are designed for a specific test environment. Changes to test data may impact test results.
3. Currently configured for sequential execution; parallel test execution is not enabled.
4. Some test steps use fixed time waits to handle page loading.
5. Only Chromium is supported. Cross-browser testing is not implemented.

---

## Project Structure
ecommerce-playwright-automation/
├── .github/workflows/
├── pages/
├── tests/
├── config/
├── reports/
├── requirements.txt
├── pytest.ini
└── README.md
