from app.ingestion.csv_loader import CSVLoader
from app.ingestion.validator import DatasetValidator


def main():

    file_path = "data/raw/online_retail_II.csv"

    df = CSVLoader.load_csv(file_path)

    DatasetValidator.validate_not_empty(df)

    print("Dataset loaded successfully.")
    print("Validation passed.")

    print(df.head())


if __name__ == "__main__":
    main()