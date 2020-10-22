# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RfidTagLotRel(models.Model):
    _name = 'dev.rfid.tag.lot.rel'
    _description = 'lot tag relation'

    lot = fields.Many2one('stock.production.lot', string='Lot')
    # tag_id = fields.One2many('dev.rfid.tag', 'tag_id', string='Tags', copy=True)
    status = fields.Boolean(string='Status')
    tag_id = fields.Many2one('dev.rfid.tag.lot.rel', string='tag id')

# class RfidTag(models.Model):
#     _inherit = 'dev.rfid.tag'
#   tag_id = fields.Many2one('dev.rfid.tag.lot.rel', string='tag id')


# lots=fields.One2many(comodel_name= 'stock.production.lot', inverse_name='product_id', string='Lots')
# lots=fields.One2many('dev_relation.dev_relation.conn','Stock_lot',string='Lots')

#
# class manyConnect(models.Model):
#     _name = 'dev_relation.dev_relation.conn'
#     _description = 'connect fields'
#
#     # lots_con=fields.Many2one('dev_relation.dev_relation',required=True)
#     Stock_lot=fields.Many2one('stock.production.lot',required=True)


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
