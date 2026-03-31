from sqlalchemy import create_engine

def load_data(df):
    print("💾 Carregando dados...")

    engine = create_engine("sqlite:///data/crypto.db")
    df.to_sql("btc_price", engine, if_exists="replace", index=False)