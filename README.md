# E-commerce Playwright Automation
E2E automation test framework for e-commerce website,
built with Python + Playwright + pytest + Page Object Model.

Fully integrated with **GitHub Actions CI/CD** for automatic testing,
report generation, and public dashboard deployment.

---

## 📊 Live Test Report (Latest CI Result)
This report is **automatically updated on every code push**.
You can view the latest test result without local setup.

👉 https://yougaaa906.github.io/ecommerce-playwright-automation/?sort=result

---

## 🚀 CI/CD Pipeline
- Automated test execution on every push / pull request
- Automatic HTML report generation
- Report deployed to GitHub Pages
- Full history & traceability

---

## 🧪 Test Coverage
### 1. User Authentication
- ✅ Login with valid credentials
- ✅ Login with invalid password
- ✅ Login with invalid username
- ✅ User logout
- ✅ Register new account
- ✅ Register with mismatched password

### 2. Product & Cart
- ✅ Homepage load & product listing
- ✅ Category filter & price sort
- ✅ Product search
- ✅ Add in-stock product to cart
- ✅ Cart quantity update & item removal
- ✅ Cart auto-cleanup after test

### 3. Checkout & UI
- ✅ Complete checkout flow validation
- ✅ Cookie consent banner display & handling
- ✅ Global cookie auto-accept for all tests

📄 **Full Test Case Document**: [View Detailed Test Cases](sslocal://flow/file_open?url=.%2Fdocs%2Ftest_cases.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

---

## 🛠 Framework Features
- Page Object Model (POM) design pattern for maintainability
- Reusable pytest fixtures (cookie handling, login, cart cleanup)
- Automatic setup/teardown with `autouse` fixtures
- Stable element locators (data-testid / aria-label) to avoid dynamic class issues
- Robust handling for overlay blocking (cart drawer, cookie banner)
- Expected failure test (`@pytest.mark.xfail`) for known price calculation defect,
  to demonstrate intentional defect validation without breaking CI pipeline
- Fully CI-stable, no flaky tests

---

## 🐛 Defect Discovery (Manual Testing)
During system familiarization, I identified several functional & UI defects in the e-commerce system,
documented with detailed steps, severity, and reproduction methods.

📋 **Full Defect Report**: [View Defect List](sslocal://flow/file_open?url=.%2Fdocs%2Fdefect_report.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

Key findings include:
- Price calculation inconsistency between cart and checkout (the basis for the XFAIL test case)
- UI layout issues on mobile view
- Edge case validation gaps in user registration

---

## 📌 Notes for Reviewers
All tests run **automatically in CI** — no local installation required.
Please check the live report link above for the latest test results.
