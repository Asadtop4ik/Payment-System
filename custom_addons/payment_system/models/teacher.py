from odoo import models, fields

class Teacher(models.Model):
    _name = 'payment_system.teacher'
    _description = 'Teacher Model'

    name = fields.Char(string="Teacher Name", required=True)
    phone = fields.Char(string="Phone Number")
    course_id = fields.Many2one('payment_system.course', string="Course")
    group_ids = fields.One2many('payment_system.group', 'teacher_id', string="Groups")
