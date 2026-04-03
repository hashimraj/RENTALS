import frappe

@frappe.whitelist()
def get_emoji():
    return "💰"

# injecting your own docTypes,,, make sure doc_events is uncommented in hooks.py and correctly include the path
def throw_emoji(doc, event):
    frappe.throw("🥲")

def send_payment_reminders():
    pass