# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class Vehicle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		color: DF.Data
		license__plate: DF.Data | None
		make: DF.Data
		model: DF.Data
		name: DF.Int | None
		title: DF.Data | None
		year: DF.Int
	# end: auto-generated types

	def before_save(self):
		self.set_title()

	def set_title(self):
		self.title = f"{self.make} {self.model}, {self.year}"