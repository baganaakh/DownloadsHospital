# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from datetime import datetime, date
_logging=logging.getLogger(__name__)

class dev_1(models.Model):
    _name = 'dev_1.dev_1'
    # _description = 'dev_1.dev_1'

    name = fields.Char(string = "Employee Name", required= True)
    plate_number = fields.Char(string="Plate number")
    enter_date = fields.Char(string = "Enter datetime")
    out_date = fields.Char(string = "Out datetime")

    status = fields.Boolean(string = "Status")
    # ads = enter_date - out_date
    # if ads > 0:
    #
    # else:
    #     status = fields.Boolean(False, store=True)
    # #status = enter_date < out_date
    #    # status = fields.Boolean(store = True)
    #     print("AS")
    # status = enter_date > out_date
    # status = fields.Boolean(status, store = True)


    # value = fields.Datetime()
    # value2 = fields.Boolean(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('enter_date')
    # def enterance(self):
    #     for record in self:
    #         record.status = bool(record.enter_date)


