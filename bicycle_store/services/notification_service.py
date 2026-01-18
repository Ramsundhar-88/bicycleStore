import frappe


def send_email(user, subject, message):
    frappe.sendmail(
        recipients=[user],
        subject=subject,
        message=message
    )


def notify_admin(subject, message):
    send_email("Administrator", subject, message)
