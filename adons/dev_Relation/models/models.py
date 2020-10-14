# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
from odoo.tools.date_utils import datetime
import logging
# from datetime import datetime, date
_logging=logging.getLogger(__name__)

class dev_1(models.Model):
    _name = 'dev_1.dev_1'
    _description = 'dfjgh;sdkfjhg;sdkf;dfjloh;'

    name = fields.Char(string = "Employee Name", required= True)
    plate_number = fields.Char(string="Plate number")
    enter_date = fields.Datetime(string = "Enter datetime")
    out_date = fields.Datetime(string = "Out datetime")

    status = fields.Boolean(string = "Status")


    # @api.depends('out_date')
    # def calculate_time(self):
    #     for rec in self:
    #         parked_time=rec.enter_date-rec.out_date
    #
    #
    # @api.constrains('out_date')
    # def check_time(self):
    #     if self.enter_date > self.out_date:
    #         raise ValidationError('Гарах цаг Орж ирсэн цагаас өмнө байж болохгүй')

    # parked_time=fields.Datetime(string='Parked_time', default=None, required=False,
    #                             readonly=True, compute='calculate_time')
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


