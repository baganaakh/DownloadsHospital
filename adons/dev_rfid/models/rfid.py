from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class rfidReader(models.Model):
    _name = 'rfid.tag'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'rfid tag lists'
    _rec_name = 'tag_name'


    tag_name=fields.Char(string='Name',required=True,track_visibility='always')
    notes=fields.Text(string='Notes',track_visibility='always')
    epc=fields.Char(string='EPC',required=True)
    _sql_constraints = [
        ('EPC_unique', 'unique(epc)', 'EPC Name already exists!')
    ]

    user=fields.Char(string='User')
    tid=fields.Char(sting='Tid')
    password=fields.Char(string='password')

    lot_ids = fields.Many2many(
        'stock.production.lot'
        , 'rfid_tag_lot_rel'
        , 'rfid_tag_id'
        , 'lot_id'
        , 'Lots'
    )
