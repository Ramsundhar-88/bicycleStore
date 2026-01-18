import frappe
from bicycle_store.config.settings import get_max_discount_percent
from bicycle_store.config.constants import ROLE_SALES_MANAGER


def get_max_item_discount(doc):
    max_discount = 0
    for item in doc.items:
        if item.discount_percentage and item.discount_percentage > max_discount:
            max_discount = float(item.discount_percentage)
    return max_discount


def validate_discount_permission(quotation_doc):
    """
    Rule:
    - Discount <= allowed -> OK
    - Discount > allowed -> only Sales Manager can submit
    """
    allowed = get_max_discount_percent()
    max_discount = get_max_item_discount(quotation_doc)

    if max_discount <= allowed:
        return

    user = frappe.session.user
    if frappe.has_role(ROLE_SALES_MANAGER, user):
        return

    frappe.throw(
        f"Discount {max_discount}% exceeds allowed limit {allowed}%. "
        f"Manager approval required."
    )


def get_customer_price_list(customer):
    """
    Optional Enhancement:
    Dealer customers can have a different price list.
    If Dealer Profile exists -> return dealer price list
    else return default selling price list.
    """
    # If your custom Dealer Profile doctype exists and linked
    if frappe.db.exists("DocType", "Dealer Profile"):
        dealer_profile = frappe.db.get_value(
            "Dealer Profile",
            {"customer": customer},
            ["price_list"],
            as_dict=True
        )
        if dealer_profile and dealer_profile.price_list:
            return dealer_profile.price_list

    # fallback to system default
    default_price_list = frappe.db.get_single_value(
        "Selling Settings", "selling_price_list"
    )
    return default_price_list
