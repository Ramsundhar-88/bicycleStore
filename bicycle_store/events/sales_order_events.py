import frappe


def validate_sales_order(doc, method=None):
    # Basic safeguard
    if not doc.customer:
        frappe.throw("Customer is required in Sales Order")
