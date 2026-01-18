import frappe

from bicycle_store.bicycle_store.config.constants import (
    DEFAULT_DRAFT_REMINDER_DAYS,
    DEFAULT_LEAD_SOURCE,
    DEFAULT_MAX_DISCOUNT_PERCENTAGE,
)

SETTINGS_DOCTYPE = "Bicycle Store Settings"

def get_settings():
    if frappe.db.exists("DocType", SETTINGS_DOCTYPE):
        return frappe.get_single(SETTINGS_DOCTYPE)
    return None

def get_max_discount_percentage():
    settings=get_settings()
    if settings and settings.max_discount_percentage:
        return float(settings.max_discount_percentage)
    return DEFAULT_MAX_DISCOUNT_PERCENTAGE

def get_default_lead_source():
    settings = get_settings()
    if settings and settings.default_lead_source:
        return settings.default_lead_source
    return DEFAULT_LEAD_SOURCE


def is_auto_sales_order_enabled():
    settings = get_settings()
    if settings and settings.enable_auto_sales_order is not None:
        return bool(settings.enable_auto_sales_order)
    return True


def is_low_stock_alert_enabled():
    settings = get_settings()
    if settings and settings.enable_low_stock_alerts is not None:
        return bool(settings.enable_low_stock_alerts)
    return False