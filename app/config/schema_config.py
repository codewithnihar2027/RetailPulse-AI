"""
RetailPulse Canonical Schema Configuration
"""


CANONICAL_SCHEMA = {

    "Invoice": {
        "required": True,
        "aliases": [
            "invoice",
            "invoice_no",
            "invoice number",
            "invoiceid",
            "order_id",
            "orderid",
            "order number",
            "bill_no"
        ]
    },

    "InvoiceDate": {
        "required": True,
        "aliases": [
            "invoice_date",
            "invoicedate",
            "order_date",
            "transaction_date",
            "date"
        ]
    },

    "CustomerID": {
        "required": True,
        "aliases": [
            "customer id",
            "customerid",
            "customer_no",
            "customer number",
            "cust_id"
        ]
    },

    "Product": {
        "required": True,
        "aliases": [
            "description",
            "product",
            "product_name",
            "item",
            "stockcode"
        ]
    },

    "Quantity": {
        "required": True,
        "aliases": [
            "quantity",
            "qty",
            "units",
            "items"
        ]
    },

    "Price": {
        "required": True,
        "aliases": [
            "price",
            "unitprice",
            "unit_price",
            "sales",
            "amount"
        ]
    },

    "Country": {
        "required": False,
        "aliases": [
            "country",
            "nation"
        ]
    }

}