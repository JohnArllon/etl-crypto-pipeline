# import pandas as pd

# def transform_data(data):
#     print("🔄 Transformando dados...")

#     btc = data["bpi"]["USD"]

#     df = pd.DataFrame([{
#         "code": btc["code"],
#         "rate": btc["rate_float"],
#         "description": btc["description"]
#     }])

#     return df

import pandas as pd

def transform_data(data):
    print("🔄 Transformando dados...")

    price = data["bitcoin"]["usd"]

    df = pd.DataFrame([{
        "crypto": "bitcoin",
        "price_usd": price
    }])

    return df