# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from datetime import date,timedelta

_logger = logging.getLogger(__name__)
class RfidTagLotRel(models.Model):
    _name = 'dev.rfid.tag.lot.rel'
    _description = 'lot tag relation'


    minday= date.today()-timedelta(days=3)
    lot_id = fields.Many2one('stock.production.lot', string='Lot')
    # status = fields.Boolean(compute='make_last', string='Status')
    status = fields.Boolean(string='Status')
    tag_id = fields.Many2one('dev.rfid.tag', string='Tag')
    product_Id=fields.Integer(compute='get_prod')

    def get_lot_id(self,tags):
        tags= self.env['dev.rfid.tag'].search([['epc', '=', 'AAA2']])
        _logger.critical('!!! str( tags ) = "' + str(tags) + '" !!!')
        lots= self.env['dev.rfid.tag.lot.rel'].search([['tag_id', '=', tags]])
        _logger.critical('!!! str( llots ) = "' + str(lots) + '" !!!')
        return lots
    # lot_id = models.execute_kw(db, uid, password, 'dev.rfid.tag.lot.rel', 'search_read',
    #                            [[['tag_id', '=', tag_id]]], {'fields': ['lot', 'tag_id']})

    def get_lots(self):
        lots=[]
        fprods=self.env['product.template'].search([('name','=','(п)')])
        _logger.critical('!!! str( fprods ) = "' + str(fprods) + '" !!!')

        for each in fprods:
            lot=self.env['stock.production.lot'].search([('product_id','=',each.id)])
            _logger.critical('!!! str( lot ) = "' + str(lot) + '" !!!')
        #     lots.append(lot.id)
        #     self.lot=lots

    @api.depends('lot_id')
    def get_prod(self):
        lotId=self.lot_id
        prod = self.env['stock.production.lot'].search([['', '=', lotId]])
        for each in prod:
            product_id=each.product_id
            _logger.critical('!!! str( product_id ) = "' + str(product_id) + '" !!!')
            return product_id
    # @api.depends('tag_id')
    # def make_last(self):
    #     results=self.env.cr.execute(
    #         'UPDATE public.dev_rfid_tag_lot_rel SET status = False WHERE tag_id = {};'%self.tag_id)
    #     _logger.critical('!!! str( update results) = "' + str(results) + '" !!!')
    #     return True
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