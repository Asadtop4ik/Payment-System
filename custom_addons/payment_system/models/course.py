from odoo import models, fields

class Course(models.Model):
    _name = 'payment_system.course'
    _description = 'Course Model'

    name = fields.Char(string="Course", required=True)
    description = fields.Text(string="Course Description")
    teacher_ids = fields.One2many('payment_system.teacher', 'course_id', string="Teachers")
    group_ids = fields.One2many('payment_system.group', 'course_id', string="Groups")
