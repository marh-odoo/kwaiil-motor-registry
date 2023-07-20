from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Motorcycle(models.Model):
    _name = "motorcycle.registry"
    _description = "Course Info two"
    _rec_name="registry_number"
    registry_number = fields.Char(string = "Registry Number", required=False, default="MRN0000", readonly=True)
    vin = fields.Char(string="",required=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customers')
    picture = fields.Image(string="", required=False)
    current_mileage = fields.Float(string="",required=False)
    license_plate = fields.Char(string="",required=False)
    certificate_title= fields.Binary()
    register_date= fields.Date(string="YYYY-MM-DD",required=False)
    brand=fields.Char(string="Brand", compute="_set_brand", readonly=True, default="")
    make=fields.Char(string="Make", compute="_set_make", readonly=True, default="")
    model=fields.Char(string="Model", compute="_set_model", readonly=True, default="")
    partner_id = fields.Many2one(comodel_name="res.partner")
    email = fields.Char(related='partner_id.email', string="Email")
    phone = fields.Char(related='partner_id.phone', string="Phone")
    owner = fields.Char(related='partner_id.name', string="Owner")
    
    _sql_constraints = [
        ('vin_verification_unique', 'UNIQUE(vin)', 'It can not be repeated VIN')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry.number')
        return super().create(vals)   
    
    @api.constrains('vin')
    def _check_vin(self):
        for record in self:
            if  not bool (re.match(r'[A-Z]{4}[0-9]{2}[0-9|A-Z]{2}[0-9]{6}', record.vin)):
                raise ValidationError("Must enter a valid vin")
            
    @api.constrains('license_plate')
    def _check_vin(self):
        for record in self:
            if  not bool (re.match(r'[A-Z]{1,4}[0-9]{1,3}[A-Z]{0,2}', record.license_plate)):
                raise ValidationError("Must enter a valid license_plate")
            
    @api.depends("vin")
    def _set_brand(self):
        for record in self:
            if record.vin:
                record.brand = record.vin[0:2]

    @api.depends("vin")
    def _set_make(self):
        for record in self:
            if record.vin:
                record.make = record.vin[2:4]

    @api.depends("vin")
    def _set_model(self):
        for record in self:
            if record.vin:
                record.model = record.vin[4:6]



            