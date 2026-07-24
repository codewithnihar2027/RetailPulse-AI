from pprint import pprint

from app.pipeline import RetailPipeline
from app.ingestion.mapper import ColumnMapper

# pipeline = RetailPipeline()

# result = pipeline.run("data/raw/online_retail_II.csv")

# print(result["mapping"])

# print(result["dataframe"].columns)
# print(result["dataframe"].dtypes)

# result = pipeline.run("data/raw/online_retail_II.csv")

# print(result["dataframe"].isnull().sum())

# result = pipeline.run("data/raw/online_retail_II.csv")

# print(result["dataframe"].columns)

# print(
#     result["dataframe"][
#         ["Quantity", "Price", "Revenue"]
#     ].head()
# )

def main():

    pipeline = RetailPipeline()

    result = pipeline.run("data/raw/online_retail_II.csv")

    # print("\n===== SCHEMA =====")

    # pprint(result["schema"])

    # print("\n===== PROFILE =====")

    # pprint(result["profile"])
    # result = pipeline.run("data/raw/online_retail_II.csv")

    # from pprint import pprint

    # print("\n===== KPIs =====")

    # pprint(result["analytics"])

    # from pprint import pprint

    # print("\n===== MONTHLY SALES =====")

    # pprint(result["analytics"]["monthly_sales"])
    # print("\n===== COUNTRY SALES =====")

    # from pprint import pprint

    # pprint(result["analytics"]["country_sales"])
    # print("\n===== TOP PRODUCTS BY REVENUE =====")
    # pprint(result["analytics"]["top_products_by_revenue"])

    # print("\n===== TOP PRODUCTS BY QUANTITY =====")
    # pprint(result["analytics"]["top_products_by_quantity"])
    # print("\n===== TOP CUSTOMERS BY REVENUE =====")
    # pprint(result["analytics"]["top_customers_by_revenue"])

    # print("\n===== TOP CUSTOMERS BY ORDERS =====")
    # pprint(result["analytics"]["top_customers_by_orders"])

    # print("\n===== RFM =====")

    # print(
    #     result["analytics"]["rfm_summary"]
    #     .head()
    # )

    # print("\n===== RFM TABLE =====")

    # print(
    #     result["analytics"]["rfm_summary"]["rfm_table"]
    #     .head()
    # )

    # print("\n===== CUSTOMER SEGMENTS =====")

    # from pprint import pprint

    # pprint(
    #     result["analytics"]["rfm_summary"]["segment_summary"]
    # )
    # print("\n===== DAILY SALES =====")
    # pprint(result["analytics"]["daily_sales"])

    # print("\n===== WEEKLY SALES =====")
    # pprint(result["analytics"]["weekly_sales"])

    # print("\n===== QUARTERLY SALES =====")
    # pprint(result["analytics"]["quarterly_sales"])

    print("\n===== MONTHLY GROWTH =====")
    pprint(result["analytics"]["monthly_growth"])

    print("\n===== SALES SUMMARY =====")
    pprint(result["analytics"]["sales_summary"])

    print("\n===== DAILY SUMMARY =====")
    pprint(result["analytics"]["daily_summary"])

    print("\n===== AVERAGE DAILY REVENUE =====")
    print(result["analytics"]["average_daily_revenue"])

if __name__ == "__main__":
    main()