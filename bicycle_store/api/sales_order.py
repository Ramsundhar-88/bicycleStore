import frappe


@frappe.whitelist()
def list_sales_orders(customer=None, limit=20):
    filters = {}
    if customer:
        filters["customer"] = customer

    return frappe.get_all(
        "Sales Order",
        filters=filters,
        fields=["name", "customer", "transaction_date", "grand_total", "status"],
        limit_page_length=int(limit),
        order_by="modified desc"
    )
