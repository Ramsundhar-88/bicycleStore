import frappe


def sales_order_exists_for_quotation(quotation_name):
    return frappe.db.exists("Sales Order", {"quotation": quotation_name})


def create_sales_order_from_quotation(quotation_doc):
    """
    Rule:
    - Create SO automatically on Quotation submit
    - Prevent duplicates
    """
    if sales_order_exists_for_quotation(quotation_doc.name):
        return None

    so = frappe.new_doc("Sales Order")
    so.customer = quotation_doc.party_name
    so.transaction_date = frappe.utils.today()
    so.delivery_date = frappe.utils.today()
    so.quotation = quotation_doc.name

    for q_item in quotation_doc.items:
        so.append("items", {
            "item_code": q_item.item_code,
            "qty": q_item.qty,
            "rate": q_item.rate,
            "discount_percentage": q_item.discount_percentage or 0,
            "warehouse": q_item.warehouse,
        })

    so.insert(ignore_permissions=True)
    so.submit()
    return so.name
