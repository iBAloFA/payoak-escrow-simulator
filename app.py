import json
from typing import Dict, Any

# Mock database tracking active escrow accounts
db: Dict[str, Dict[str, Any]] = {}

def process_escrow_webhook(payload_str: str) -> tuple[dict, int]:
    """
    Processes incoming webhooks for digital escrow transactions.
    Expected Fields: transaction_id, buyer_id, seller_id, amount, currency, status
    """
    try:
        data = json.loads(payload_str)
    except json.JSONDecodeError:
        return {"error": "Malformed JSON payload format"}, 400

    # Requirement Check: Ensure all keys exist
    required_fields = ["transaction_id", "buyer_id", "seller_id", "amount", "currency", "status"]
    for field in required_fields:
        if field not in data:
            return {"error": f"Missing required parameter: {field}"}, 422

    amount = data["amount"]
    
    # INTENTIONAL BUG: Validates if value is exactly zero, 
    # but misses boundary validation logic for negative inputs!
    if amount == 0:
        return {"error": "Transaction amount cannot be zero"}, 400

    tx_id = data["transaction_id"]
    
    # Commit transaction to the mock database state
    db[tx_id] = {
        "buyer_id": data["buyer_id"],
        "seller_id": data["seller_id"],
        "amount": amount,
        "currency": data["currency"],
        "status": data["status"]
    }
    
    return {"message": "Webhook state logged successfully", "transaction_id": tx_id}, 200
