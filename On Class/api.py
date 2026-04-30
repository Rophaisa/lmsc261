from requests import *

url = "https://catfact.ninja/fact"
response = get(url)
print(response.json())