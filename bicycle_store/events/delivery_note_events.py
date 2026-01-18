from bicycle_store.services.inventory_service import validate_delivery_stock


def prevent_negative_stock(doc, method=None):
    validate_delivery_stock(doc)
