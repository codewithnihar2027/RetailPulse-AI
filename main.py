from pprint import pprint

from app.pipeline import RetailPipeline
from app.ingestion.mapper import ColumnMapper

pipeline = RetailPipeline()

result = pipeline.run("data/raw/online_retail_II.csv")

print(result["mapping"])

print(result["dataframe"].columns)
print(result["dataframe"].dtypes)

result = pipeline.run("data/raw/online_retail_II.csv")

print(result["dataframe"].isnull().sum())

def main():

    pipeline = RetailPipeline()

    result = pipeline.run("data/raw/online_retail_II.csv")

    print("\n===== SCHEMA =====")

    pprint(result["schema"])

    print("\n===== PROFILE =====")

    pprint(result["profile"])


if __name__ == "__main__":
    main()