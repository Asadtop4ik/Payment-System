from email.policy import default

from odoo import fields, models, api
from odoo.tools import unique


class Student(models.Model):
    _name = 'wb.student'
    _description = "this is a student model"


    @api.model
    def _get_vip_list(self):
        return [("vip", "VIP")]

    name = fields.Char("Name")
    name1 = fields.Char("Name1")
    name2 = fields.Char("Name2")
    name3 = fields.Char("Name3")
    name4 = fields.Char("Name4")

    student_name = fields.Char(size=4)
    address = fields.Text(help="Address of the student")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], default='female',
    )
    roll_number = fields.Integer()
    advance_gender = fields.Selection("_get_advance_gender")
    vip = fields.Selection(
        _get_vip_list
    )
    student_fees = fields.Float("Fees")
    address_html = fields.Html("Address HTML")

    def _get_advance_gender(self):
        return [("male", "Male"), ("female", "Female")]