from bicycle_store.services.inventory_service import get_low_stock_items
from bicycle_store.services.notification_service import notify_admin
from bicycle_store.config.settings import is_low_stock_alert_enabled


def send_low_stock_alerts():
    if not is_low_stock_alert_enabled():
        return

    low_stock = get_low_stock_items(limit=20)
    if not low_stock:
        return

    notify_admin(
        "Low Stock Alert - Bicycle Store",
        f"<pre>{low_stock}</pre>"
    )
