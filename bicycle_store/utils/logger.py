import frappe


def get_logger():
    return frappe.logger("bicycle_store", allow_site=True, file_count=10)
