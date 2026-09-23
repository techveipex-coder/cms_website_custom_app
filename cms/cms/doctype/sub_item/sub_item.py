import re

import frappe
from frappe.model.document import Document


class SubItem(Document):
    def before_save(self):
        self.slug = self.create_slug(self.name)

    @staticmethod
    def create_slug(value):
        value = value.strip().lower()
        value = re.sub(r"[^a-z0-9]+", "-", value)
        value = re.sub(r"-+", "-", value)
        return value.strip("-")