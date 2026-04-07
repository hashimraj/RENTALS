# Copyright (c) 2026, ALS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class VirtualEmployee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		emp_code: DF.Data | None
	# end: auto-generated types

	
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self, *args, **kwargs):
		pass

	def db_update(self, *args, **kwargs):
		pass

	def delete(self, *args, **kwargs):
		pass

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
		pass

	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass

