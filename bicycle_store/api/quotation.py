import frappe


@frappe.whitelist()
def get_quotation(name):
    return frappe.get_doc("Quotation", name).as_dict()


@frappe.whitelist()
def list_quotations(customer=None, limit=20):
    filters = {}
    if customer:
        filters["party_name"] = customer

    return frappe.get_all(
        "Quotation",
        filters=filters,
        fields=["name", "party_name", "transaction_date", "grand_total", "status"],
        limit_page_length=int(limit),
        order_by="modified desc"
    )
