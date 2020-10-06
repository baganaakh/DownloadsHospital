from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name=fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Өвчитний жагсаалт'
    _rec_name = 'patient_name'

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('The Age Must be Greater than 5'))

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group='minor'
                else:
                    rec.age_group='major'


    patient_name=fields.Char(string='Patient Name',required=True,track_visibility='always')
    patient_age=fields.Integer('Age',track_visibility='always')
    notes=fields.Text(string='Notes')
    image=fields.Binary(string='Image',attachment=True)
    name=fields.Char(string='testName')
    name_seq=fields.Char(string='Order Reference', required=True, copy=False,
                         readonly=True, index=True, default=lambda self: _('New'))
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], default='male', string="Gender")
    age_group=fields.Selection([
        ('major','Major'),
        ('minor','Minor')
    ], string='Age Group',compute='set_age_group')


    # How    to    Add    New    Sequence in odoo12
    @ api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
                vals['name_seq']=self.env['ir.sequence'].next_by_code('hospital.patient.sequence')or _('new')
        result=super(HospitalPatient, self).create(vals)
        return result