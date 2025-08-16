"""Client for interacting with the iiko API."""

import requests
from config import IIKO_URL, IIKO_TOKEN, COMPANY_ID

def send_document(data):
    """Placeholder for sending data to iiko."""
    headers = {"Authorization": f"Bearer {IIKO_TOKEN}"}
    try:
        response = requests.post(IIKO_URL, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        return {"error": str(exc)}
