import json
from app import process_escrow_webhook, db

def run_qa_test_suite():
    print("=" * 65)
    print("RUNNING: ESCROW API TRANSACTION VALIDATION TEST SUITE")
    print("=" * 65)

    # TEST CASE 1: Happy Path Validation
    print("\n[TC-01] Executing Happy Path Test...")
    happy_payload = {
        "transaction_id": "tx-payoak-1001",
        "buyer_id": "buyer_90",
        "seller_id": "seller_45",
        "amount": 75000.00,
        "currency": "NGN",
        "status": "initiated"
    }
    res, status = process_escrow_webhook(json.dumps(happy_payload))
    print(f"Result Status: {status} | Server Response: {res}")
    assert status == 200, "TC-01 Failed"

    # TEST CASE 2: Negative Testing (Missing Key Parameters)
    print("\n[TC-02] Executing Missing Schema Key Test...")
    broken_payload = {
        "transaction_id": "tx-payoak-1002",
        "buyer_id": "buyer_90",
        "amount": 2000.00
    }
    res, status = process_escrow_webhook(json.dumps(broken_payload))
    print(f"Result Status: {status} | Server Response: {res}")
    assert status == 422, "TC-02 Failed"

    # TEST CASE 3: Boundary Value Exploitation (The Discovered Bug)
    print("\n[TC-03] Executing Boundary Value Bug Detection Test...")
    exploit_payload = {
        "transaction_id": "tx-payoak-1003",
        "buyer_id": "buyer_90",
        "seller_id": "seller_45",
        "amount": -50000.00,  # Negative value field anomaly
        "currency": "NGN",
        "status": "initiated"
    }
    res, status = process_escrow_webhook(json.dumps(exploit_payload))
    print(f"Result Status: {status} | Server Response: {res}")
    
    # QA Assertion to isolate state corruptions
    if status == 200 and db.get("tx-payoak-1003", {}).get("amount", 0) < 0:
        print("\n❌ CRITICAL SECURITY VULNERABILITY ISOLATED!")
        print(f"System allowed negative balance payload to commit to DB: {db['tx-payoak-1003']}")
    else:
        print("\n✅ System safely restricted invalid payload execution.")

    print("\n" + "=" * 65)
    print("TEST SUITE EXECUTION CONCLUDED")
    print("=" * 65)

if __name__ == "__main__":
    run_qa_test_suite()
