from odoo import models, fields

class Group(models.Model):
    _name = 'payment_system.group'
    _description = 'Group Model'

    name = fields.Char(string="Group", required=True)
    course_id = fields.Many2one('payment_system.course', string="Course")
    teacher_id = fields.Many2one('payment_system.teacher', string="Teacher")
    student_ids = fields.Many2many('payment_system.student', string="Students")
    payment_ids = fields.One2many('payment_system.payment', 'group_id', string="Payments")
