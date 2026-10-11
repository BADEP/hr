# Copyright 2023 Tecnativa - Víctor Martínez
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class IrAccess(models.Model):
    _inherit = "ir.access"

    def _get_access_context(self):
        # hr.employee._access_domain() depends on this context key
        yield from super()._get_access_context()
        yield bool(self.env.context.get("search_attachments_from_hr_employee"))
