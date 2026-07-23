from pprint import pprint

from app.pipeline import RetailPipeline


def main():

    pipeline = RetailPipeline()

    result = pipeline.run("data/raw/online_retail_II.csv")

    print("\n===== SCHEMA =====")

    pprint(result["schema"])

    print("\n===== PROFILE =====")

    pprint(result["profile"])


if __name__ == "__main__":
    main()