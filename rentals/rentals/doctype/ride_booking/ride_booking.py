# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RideBooking(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from rentals.rentals.doctype.ride_booking_item.ride_booking_item import RideBookingItem

        amended_from: DF.Link | None
        driver: DF.Link
        items: DF.Table[RideBookingItem]
        order: DF.Link
        rate: DF.Currency
        still_editable: DF.Data | None
        total_amount: DF.Currency
        vehicle: DF.Link | None
    # end: auto-generated types

    def validate(self):
        """Calculate total_amount based on items and rate"""

        # Ensure rate is provided
        if not self.rate:
            frappe.throw("Please provide a rate")

        # Calculate total distance from all items
        total_distance = sum(item.distance for item in self.items if item.distance)

        # Calculate total_amount
        self.total_amount = total_distance * self.rate