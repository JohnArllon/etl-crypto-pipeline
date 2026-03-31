# import requests

# def extract_data():
#     print("📥 Extraindo dados da API...")

#     url = "https://api.coindesk.com/v1/bpi/currentprice.json"
#     response = requests.get(url)

#     return response.json()

# import requests

# def extract_data():
#     print("📥 Extraindo dados da API...")

#     url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         print(f"❌ Erro na API: {e}")
#         return None
    
    # return None
    # response = requests.get(url)

    # return response.json()

import requests
import json

def extract_data():
    print("📥 Extraindo dados da API...")

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # 👉 NOVO: salvar dados brutos
        with open("data/raw/data.json", "w") as f:
            json.dump(data, f)

        return data

    except Exception as e:
        print(f"❌ Erro na API: {e}")
        return None