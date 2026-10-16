# Copyright (C) 2017-Today: Odoo Community Association (OCA)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

from odoo.addons.web.controllers.database import scan_languages


class HrEmployeeLanguage(models.Model):
    _name = "hr.employee.language"
    _description = "HR Employee Language"

    name = fields.Selection(scan_languages(), string="Language", required=True)
    description = fields.Char()
    employee_id = fields.Many2one("hr.employee", required=True)
    can_read = fields.Boolean(string="Read", default=True)
    can_write = fields.Boolean(string="Write", default=True)
    can_speak = fields.Boolean(string="Speak", default=True)
    can_listen = fields.Boolean(string="Listen", default=True)
