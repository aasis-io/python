import requests

from fact import Fact 

api_url = "https://catfact.ninja/fact"
response = requests.get(api_url)

print(response.status_code)

def get_random_advice(url):
    if response.status_code == 200:
        data = response.json()
        fact = Fact(data)
        return fact
    else:
        return None
    # print(response.json())

random_fact = get_random_advice(api_url)
print(random_fact)