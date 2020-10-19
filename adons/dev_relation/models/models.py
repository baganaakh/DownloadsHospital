# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dev_relation(models.Model):
    _name = 'dev_relation.dev_relation'
    _description = 'dev_relation.dev_relation'

    tag_id=fields.Many2one('rfid.tag', string='Tag')
    active=fields.Boolean(string='Active')
    lots=fields.One2many('dev_relation.dev_relation.conn','lots_con',string='Lots')

class manyConnect(models.Model):
    _name = 'dev_relation.dev_relation.conn'
    _description = 'connect fields'
    lots_con=fields.Many2one('stock.production.lot','name',required=True)




#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

