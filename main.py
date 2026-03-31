from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

    print("✅ Pipeline finalizado!")

if __name__ == "__main__":
    run_pipeline()