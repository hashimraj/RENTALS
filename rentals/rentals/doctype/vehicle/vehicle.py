# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		audit_completed: DF.Check
		color: DF.Data
		condition: DF.Rating
		insurance_expiry: DF.Date
		is_published: DF.Check
		license__plate: DF.Data | None
		make: DF.Data
		model: DF.Data
		name: DF.Int | None
		route: DF.Data | None
		status: DF.Literal["Active", "Out of Service", "Sold", "Crushed"]
		title: DF.Data | None
		vehicle_image: DF.AttachImage | None
		year: DF.Int
	# end: auto-generated types

	def before_save(self):
		self.set_title()

	def set_title(self):
		self.title = f"{self.make} {self.model}, {self.year}"