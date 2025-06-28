import requests

# Test /data endpoint (Base64 encode)
url = "http://127.0.0.1:5000/data"
payload = {"data": "hell0"}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Raw Response:", response.text)

try:
    print("JSON Response:", response.json())
except Exception as e:
    print("Error decoding JSON:", str(e))
