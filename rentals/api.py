import frappe

@frappe.whitelist()
def get_emoji():
    return "💰"

def throw_emoji(doc, event):
    frappe.throw("🥲")