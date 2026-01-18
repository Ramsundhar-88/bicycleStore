import frappe


def is_dealer_customer(customer):
    """
    If Dealer Profile exists for this customer -> dealer
    """
    if not frappe.db.exists("DocType", "Dealer Profile"):
        return False

    return bool(frappe.db.exists("Dealer Profile", {"customer": customer}))


def validate_customer_credit_limit(customer):
    """
    Optional Enhancement:
    Restrict orders if outstanding exceeds credit limit.
    ERPNext has credit limit feature already, this is custom check.
    """
    credit_limit = frappe.db.get_value("Customer", customer, "credit_limit") or 0
    if not credit_limit:
        return

    outstanding = frappe.db.get_value("Customer", customer, "outstanding_amount") or 0

    if float(outstanding) > float(credit_limit):
        frappe.throw(
            f"Customer credit limit exceeded. Outstanding: {outstanding}, Limit: {credit_limit}"
        )
