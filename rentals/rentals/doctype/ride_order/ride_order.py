# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideOrder(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		contact_number: DF.Phone
		customer_name: DF.Data
		pickup_address: DF.SmallText
		pickup_time: DF.Datetime
		status: DF.Literal["New", "Accepted", "Rejected"]
		vehicle: DF.Link | None
	# end: auto-generated types

