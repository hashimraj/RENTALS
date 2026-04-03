# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    # Debug (optional)
    frappe.errprint(filters)

    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data"
        },
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "options": "AED"
        }
    ]

    # ✅ Use SQL to correctly join Vehicle
    data = frappe.db.sql("""
        SELECT 
            v.make AS make, 
            SUM(rb.total_amount) AS total_revenue
        FROM `tabRide Booking` rb
        LEFT JOIN `tabVehicle` v ON rb.vehicle = v.name
        WHERE rb.docstatus = 1
        GROUP BY v.make
        ORDER BY total_revenue DESC
    """, as_dict=True)

    # Debug data (uncomment if needed)
    # print(data)

    # ✅ Safe chart generation
    chart = {
        "data": {
            "labels": [d.get("make") or "Unknown" for d in data],
            "datasets": [
                {
                    "name": "Total Revenue",
                    "values": [d.get("total_revenue") or 0 for d in data],
                }
            ],
        },
        "type": "pie",
    }

    # ✅ Correct return order
    return columns, data, None, chart, None