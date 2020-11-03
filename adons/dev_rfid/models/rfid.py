from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class RfidTag(models.Model):
    _name = 'dev.rfid.tag'
    _description = 'rfid tag lists'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'tag_name'

    name = fields.Char(string='Name', required=True, track_visibility='always')
    notes = fields.Text(string='Notes', track_visibility='always')
    epc = fields.Char(string='EPC', required=True)
    _sql_constraints = [
        ('EPC_unique', 'unique(epc)', 'EPC Name already exists!')
    ]

    user = fields.Char(string='User')
    tid = fields.Char(sting='Tid')
    password = fields.Char(string='Tag Password')
    # tag_id=fields.Many2one('dev.rfid.tag.lot.rel',string='tag_id')
    # @api.multi
    # def name_get(self):
    #     res = []
    #     for field in self:
    #         res.append((field.id, '%s %s' % (field.tag_name, field.epc)))
    #     return res
# class RfidTagLotRel(models.Model):
#     _inherit = 'dev.rfid.tag.lot.rel'
#
#     tag_list = fields.One2many('dev.rfid.tag', 'tag_id', string='Tag', copy=True)
#


# order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade', index=True, copy=False)
#     order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines',
#                                  states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
#     tag_id = fields.Many2one('dev.rfid.tag', required=True, ondelete='cascade', index=True, copy=False)
# lot_12m=fields.One2many('sale.order.line', 'order_id',string='lot one2many')
# lot_ids = fields.Many2many(
#     'stock.production.lot'
#     , 'rfid_tag_lot_rel'
#     , 'tag_id'
#     , 'lot_id'
#     , 'Lots'
# )

# lot_m21=fields.Many2one('stock.production.lot',string='lot many2one')
# class tagLotRel(models.Model):
#     _name = 'rfid_tag_lot_rel'
#     _description = 'relation of the tag_ID and lot_id'
#
#     tag_id=fields.Integer()
#     lot_id=fields.Integer()

#     product_id=fields.Many2one('product.template',string='Products')
#     order_id = fields.Many2one('sale.order', string='Order Reference', required=True,
#                                   ondelete='cascade', index=True, copy=False)
