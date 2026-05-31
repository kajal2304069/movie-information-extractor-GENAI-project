import requests

try:
    r = requests.get("https://huggingface.co", timeout=10)
    print("Status:", r.status_code)
except Exception as e:
    print("Error:", e)