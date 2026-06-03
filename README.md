# PayOak Escrow API Transaction Validation Simulator

A specialized Quality Assurance (QA) demonstration framework designed to simulate an asynchronous fintech payment gateway processing escrow-powered webhook payloads. This project isolates infrastructure integration challenges, performs boundary value analysis, and models a production-grade bug-tracking report lifecycle.

## 📌 Project Overview
Fintech systems require rigid input validation routines to protect against financial ledger discrepancies. This repository demonstrates:
- A functional Python backend module (`app.py`) managing mock escrow transaction operations.
- An automated boundary testing harness (`run_tests.py`) evaluating edge-case criteria.
- A formalized QA defect report (`BUG_REPORT.md`) logging a critical input-handling vulnerability.

## 🛠️ Tech Stack & QA Methodologies
- **Language:** Python 3.x
- **Core Modules:** `json`, `typing`
- **Testing Typologies:** Integration Testing, Functional Verification, Boundary Value Analysis (BVA), Negative Path Testing, and Error Guessing.
- **Workflow Tools Alignment:** Ready for integration with defect-tracking systems like **Jira**, **Trello**, or **ClickUp**.

## 🚦 Test Suites & Edge Cases Addressed


| Test Case ID | Test Objective | Target Vector | Expected Result | Pass/Fail Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Happy Path Verification | Valid transaction payload | `HTTP 200 OK` State committed | **PASS** |
| **TC-02** | Structural Schema Validation | Missing required JSON keys | `HTTP 422 Unprocessable` | **PASS** |
| **TC-03** | Boundary Value Exploitation | Negative financial amounts (`< 0`) | `HTTP 400 Bad Request` | **FAIL (Bug Isolated)** |

## 🚀 Execution Instructions

To execute the test suite script and review the QA runtime diagnostics, navigate to your root folder and run the command line runner:

```bash
python run_tests.py
```

### Expected Output Terminal Log:
```text
=================================================================
RUNNING: ESCROW API TRANSACTION VALIDATION TEST SUITE
=================================================================

[TC-01] Executing Happy Path Test...
Result Status: 200 | Server Response: {'message': 'Webhook state logged successfully', 'transaction_id': 'tx-payoak-1001'}

[TC-02] Executing Missing Schema Key Test...
Result Status: 422 | Server Response: {'error': 'Missing required parameter: seller_id'}

[TC-03] Executing Boundary Value Bug Detection Test...
Result Status: 200 | Server Response: {'message': 'Webhook state logged successfully', 'transaction_id': 'tx-payoak-1003'}

❌ CRITICAL SECURITY VULNERABILITY ISOLATED!
System allowed negative balance payload to commit to DB: {'buyer_id': 'buyer_90', 'seller_id': 'seller_45', 'amount': -50000.0, 'currency': 'NGN', 'status': 'initiated'}

=================================================================
TEST SUITE EXECUTION CONCLUDED
=================================================================
```

## 📝 Defect Lifecycle Documentation
Full documentation on the discovered boundary parameter exploit loop, step-by-step reproduction flows, and production source code remedies are explicitly mapped inside the [BUG_REPORT.md](./BUG_REPORT.md) module.
