import time
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    data = extract_data()

    if data is None:
        print("❌ Falha na extração")
        return

    df = transform_data(data)
    data = extract_data()
    df = transform_data(data)
    load_data(df)
    print("✅ Pipeline finalizado!")

if __name__ == "__main__":
    while True:
        run_pipeline()
        print("⏳ Rodando novamente em 60 segundos...")
        time.sleep(60)