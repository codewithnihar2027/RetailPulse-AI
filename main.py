from pprint import pprint

from app.ingestion.csv_loader import CSVLoader
from app.ingestion.validator import DatasetValidator
from app.ingestion.schema import SchemaDetector
from app.ingestion.profiler import DataProfiler


def main():

    file_path = "data/raw/online_retail_II.csv"

    df = CSVLoader.load_csv(file_path)

    DatasetValidator.validate_not_empty(df)

    print("\n===== SCHEMA REPORT =====")
    pprint(SchemaDetector.generate_report(df))

    print("\n===== DATA PROFILE =====")
    pprint(DataProfiler.generate_profile(df))


if __name__ == "__main__":
    main()