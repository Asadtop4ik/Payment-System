from odoo import models, fields

class Student(models.Model):
    _name = 'payment_system.student'
    _description = 'Student Model'

    name = fields.Char(string="Student Name", required=True)
    phone = fields.Char(string="Phone Number")
    group_ids = fields.Many2many('payment_system.group', string="Groups")
    payment_ids = fields.One2many('payment_system.payment', 'student_id', string="Payments")
