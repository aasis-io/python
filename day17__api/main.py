import requests

from advice import Advice 

api_url = "http://api.adviceslip.com/advice"
response = requests.get(api_url)

print(response.status_code)

def get_random_advice(url):
    if response.status_code == 200:
        data = response.json()
        advice = Advice(data)
        return advice
    else:
        return None
    # print(response.json())

random_advice = get_random_advice(api_url)
print(random_advice)