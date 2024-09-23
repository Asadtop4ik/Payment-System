from odoo import models, fields

class Participant(models.Model):
    _name = 'himmat.participant'
    _description = 'Participant'

    name = fields.Char(string='Participant Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    group_id = fields.Many2one('himmat.group', string='Group')
