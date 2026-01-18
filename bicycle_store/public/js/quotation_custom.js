frappe.ui.form.on("Quotation", {
    validate(frm) {
        let max_discount = 15;
        let max_item_discount = 0;

        (frm.doc.items || []).forEach(row => {
            if (row.discount_percentage > max_item_discount) {
                max_item_discount = row.discount_percentage;
            }
        });

        if (max_item_discount > max_discount) {
            frappe.msgprint({
                title: "Discount Approval Required",
                message: `Discount ${max_item_discount}% exceeds allowed ${max_discount}%. Only Sales Manager can submit.`,
                indicator: "red"
            });
        }
    }
});
