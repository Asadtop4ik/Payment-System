from odoo import models, fields

class Group(models.Model):
    _name = 'himmat.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    description = fields.Text(string='Description')
    participant_ids = fields.One2many('himmat.participant', 'group_id', string='Participants')
