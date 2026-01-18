import frappe


def create_approval_request(reference_doctype, reference_name, reason):
    if not frappe.db.exists("DocType", "Approval Request"):
        return None

    req = frappe.new_doc("Approval Request")
    req.reference_doctype = reference_doctype
    req.reference_name = reference_name
    req.reason = reason
    req.status = "Pending"
    req.insert(ignore_permissions=True)
    return req.name
