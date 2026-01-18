import frappe


def get_max_item_discount(quotation_doc):
    max_discount = 0
    for item in quotation_doc.items:
        if item.discount_percentage and item.discount_percentage > max_discount:
            max_discount = item.discount_percentage
    return max_discount
