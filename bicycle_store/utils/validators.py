import frappe


def ensure_role(role_name: str, user: str = None):
    user = user or frappe.session.user
    if not frappe.has_role(role_name, user):
        frappe.throw(f"Permission denied. Required role: {role_name}")
