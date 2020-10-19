# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)

class DevModelname(models.Model):
    _name = 'dev.modelname'
    _description = 'Development model-name'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
    @api.depends('value')
    def _value_pc(self):
        _logger.critical('!!! 20 str( self )  = "' + str( self ) + '" !!!')
        for record in self:
            record.value2 = float(record.value) / 100
