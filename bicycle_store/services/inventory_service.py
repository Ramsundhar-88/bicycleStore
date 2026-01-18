import frappe


def get_available_qty(item_code, warehouse):
    qty = frappe.db.get_value(
        "Bin",
        {"item_code": item_code, "warehouse": warehouse},
        "actual_qty"
    )
    return float(qty or 0)


def validate_delivery_stock(doc):
    """
    Rule:
    Delivery should not be performed if stock is insufficient
    """
    for item in doc.items:
        if not item.warehouse:
            continue

        available = get_available_qty(item.item_code, item.warehouse)
        if float(item.qty) > available:
            frappe.throw(
                f"Insufficient stock for {item.item_code} in {item.warehouse}. "
                f"Available: {available}, Required: {item.qty}"
            )


def get_low_stock_items(limit=30):
    """
    Basic low stock check.
    (Better approach: use ERPNext Reorder Level feature.)
    """
    return frappe.db.sql("""
        SELECT item_code, warehouse, actual_qty
        FROM `tabBin`
        WHERE actual_qty <= 0
        LIMIT %s
    """, (int(limit),), as_dict=True)
