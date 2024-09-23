from odoo import models, fields

class IncomeExpense(models.Model):
    _name = 'payment_system.income_expense'
    _description = 'Income and Expense Model'

    name = fields.Char(string="Description", required=True)
    type = fields.Selection([('income', 'Income'), ('expense', 'Expense')], string="Type", required=True)
    amount = fields.Float(string="Amount", required=True)
    date = fields.Date(string="Date", default=fields.Date.context_today)
    teacher_id = fields.Many2one('payment_system.teacher', string="Teacher")
