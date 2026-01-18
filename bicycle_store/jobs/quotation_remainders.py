import frappe
from frappe.utils import nowdate, add_days
from bicycle_store.config.settings import get_draft_reminder_days


def send_pending_quotation_reminders():
    days = get_draft_reminder_days()
    cutoff = add_days(nowdate(), -days)

    quotations = frappe.get_all(
        "Quotation",
        filters={
            "docstatus": 0,
            "transaction_date": ("<=", cutoff)
        },
        fields=["name", "owner", "customer_name", "transaction_date"]
    )

    for q in quotations:
        frappe.sendmail(
            recipients=[q.owner],
            subject=f"Pending Quotation Reminder: {q.name}",
            message=f"""
                <p>Quotation <b>{q.name}</b> is still in Draft since <b>{q.transaction_date}</b>.</p>
                <p>Please follow up and submit if required.</p>
            """
        )
