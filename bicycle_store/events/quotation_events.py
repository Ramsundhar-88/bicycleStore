from bicycle_store.services.pricing_service import validate_discount_permission
from bicycle_store.services.sales_order_service import create_sales_order_from_quotation
from bicycle_store.config.settings import is_auto_sales_order_enabled


def validate_discount_rules(doc, method=None):
    validate_discount_permission(doc)


def auto_create_sales_order(doc, method=None):
    if not is_auto_sales_order_enabled():
        return

    create_sales_order_from_quotation(doc)
