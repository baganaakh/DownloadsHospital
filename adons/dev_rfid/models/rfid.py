from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class rfidReader(models.Model):
    _name = 'dev.rfid.tag'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'rfid tag lists'
    _rec_name = 'tag_name'


    tag_name=fields.Char(string='Name',required=True,track_visibility='always')
    notes=fields.Text(string='Notes',track_visibility='always')
    # name_seq=fields.Char(string='Order Reference', required=True, copy=False,
    #                      readonly=True, index=True, default=lambda self: _('New'))
    epc=fields.Char(string='EPC',required=True)
    _sql_constraints = [
        ('EPC_unique', 'unique(epc)', 'EPC Name already exists!')
    ]
    user=fields.Char(string='User')
    tid=fields.Char(sting='Tid')
    password=fields.Char(string='password')

    # How    to    Add    New    Sequence in odoo12
    # @ api.model
    # def create(self, vals):
    #     if vals.get('name_seq', _('New')) == _('New'):
    #             vals['name_seq'] = self.env['ir.sequence'].next_by_code('rfid.tag.sequence') or _('new')
    #     result = super(rfidReader, self).create(vals)
    #     return result