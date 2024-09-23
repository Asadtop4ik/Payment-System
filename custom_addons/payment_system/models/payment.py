from odoo import models, fields

class Payment(models.Model):
    _name = 'payment_system.payment'
    _description = 'Payment Model'

    student_id = fields.Many2one('payment_system.student', string="Student", required=True)
    group_id = fields.Many2one('payment_system.group', string="Group", required=True)
    date = fields.Date(string="Payment Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount", required=True)
    check_number = fields.Char(string="Check Number")
    notes = fields.Text(string="Payment Notes")
