import requests
import pandas as pd

url = "https://api.hellopeter.com/api/consumer/business/capitec-bank/reviews"

result=[]
for x in range(1, 343):
    querystring = {"page":f"{x}"}

    payload = ""
    headers = {
        "authority": "api.hellopeter.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.hellopeter.com",
        "referer": "https://www.hellopeter.com/",
        "sec-ch-ua": "^\^Google"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(str(x))

    dt = response.json()
    for review in dt['data']:
        result.append(review)
        print(len(result))
        df = pd.json_normalize(result)
        df.to_csv('Capitec_Bank_dataset.csv', index=False)