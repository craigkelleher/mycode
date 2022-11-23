import requests
URL="http://127.0.0.1:2224/pikachu"

resp= requests.get(URL)

print(resp.json())
