frappe.ui.form.on("Sales Order", {
    refresh(frm) {
        if (frm.doc.quotation) {
            frm.add_custom_button("Open Quotation", () => {
                frappe.set_route("Form", "Quotation", frm.doc.quotation);
            });
        }
    }
});
