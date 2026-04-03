// Copyright (c) 2026, ALS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {

	},

    get_summary(frm) {
        frm.get_field("summary").$wrapper.append("<h3>Here is your summary</h3>")
    }
});
