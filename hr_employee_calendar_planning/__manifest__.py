# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Employee Calendar Planning",
    "version": "20.0.1.0.0",
    "category": "Human Resources",
    "website": "https://github.com/OCA/hr",
    "author": "Tecnativa,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr"],
    "data": [
        "views/hr_employee_views.xml",
        "views/resource_calendar_views.xml",
        'security/ir.access.csv',
    ],
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "maintainers": ["victoralmau", "pedrobaeza"],
}
