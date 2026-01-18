import frappe


@frappe.whitelist()
def ping():
    return {"status": "ok", "app": "bicycle_store"}
