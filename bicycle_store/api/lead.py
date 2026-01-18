import frappe


@frappe.whitelist()
def create_lead(lead_name, mobile_no=None, source=None):
    lead = frappe.new_doc("Lead")
    lead.lead_name = lead_name
    lead.mobile_no = mobile_no
    if source:
        lead.source = source
    lead.insert(ignore_permissions=True)
    return lead.name
