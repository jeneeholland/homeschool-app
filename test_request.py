import requests

print("Starting test...")

response = requests.get("https://api.open-meteo.com", timeout=10)

print("Status code:", response.status_code)
print("Done")