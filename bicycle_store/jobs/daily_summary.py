import frappe
from frappe.utils import nowdate


def send_daily_summary():
    today = nowdate()

    sales_count = frappe.db.count("Sales Invoice", {"posting_date": today, "docstatus": 1})
    quotation_count = frappe.db.count("Quotation", {"transaction_date": today})

    msg = f"""
    <h3>Daily Summary ({today})</h3>
    <ul>
        <li>Sales Invoices Submitted: <b>{sales_count}</b></li>
        <li>Quotations Created: <b>{quotation_count}</b></li>
    </ul>
    """

    # Send to Administrator only
    frappe.sendmail(
        recipients=["Administrator"],
        subject=f"Daily Summary - {today}",
        message=msg
    )
