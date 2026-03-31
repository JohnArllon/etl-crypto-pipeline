# import requests

# def extract_data():
#     print("📥 Extraindo dados da API...")

#     url = "https://api.coindesk.com/v1/bpi/currentprice.json"
#     response = requests.get(url)

#     return response.json()

import requests

def extract_data():
    print("📥 Extraindo dados da API...")

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    response = requests.get(url)

    return response.json()