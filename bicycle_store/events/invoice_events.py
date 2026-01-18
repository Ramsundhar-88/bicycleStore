import frappe


def validate_invoice(doc, method=None):
    if not doc.customer:
        frappe.throw("Customer is required for Sales Invoice")
