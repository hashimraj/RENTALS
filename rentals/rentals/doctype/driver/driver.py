# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		enabled: DF.Check
		first_name: DF.Data
		last_name: DF.Data | None
		license_number: DF.Data
		phone_number: DF.Phone | None
		profile_image: DF.AttachImage | None
	# end: auto-generated types

	@property
	def full_name(self):
		print("FULL NAME CALLED")
		return f"{self.first_name} {self.last_name}"

	def send_alert(self):
		print("sending message")