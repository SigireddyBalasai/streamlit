import hashlib
import requests

def generate_customer_id(email):
    # Generate a unique customer ID from the email using hashlib
    customer_id = hashlib.sha256(email.encode()).hexdigest()
    return customer_id

def create_upi_qr_code(email):
    url = "https://api.razorpay.com/v1/payments/qr_codes"
    auth = ("rzp_test_6e0F6btGeOqxoh", "LHOTV90lmfTNAF2Ww3gmQnzS")
    headers = {
        "Content-Type": "application/json"
    }
    
    # Generate customer ID based on email
    customer_id = generate_customer_id(email)
    
    data = {
        "type": "upi_qr",
        "name": "Store Front Display",
        "usage": "single_use",
        "fixed_amount": True,
        "payment_amount": 50,
        "description": "For Store 1",
        "customer_id": customer_id,  # Use generated customer ID
        "notes": {
            "purpose": "Test UPI QR Code notes",
            "email": email
        }
    }

    response = requests.post(url, auth=auth, headers=headers, json=data)

    return response.json()


if __name__ == "__main__":
    ok = create_upi_qr_code("sigireddybalasai@gmail.com")
    print(ok)
