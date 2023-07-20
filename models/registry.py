from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Motorcycle(models.Model):
    _name = "motorcycle.registry"
    _description = "Course Info two"
    _rec_name="registry_number"
    registry_number = fields.Char(string = "Name", required=False, default="MRN0000", readonly=True)
    vin = fields.Char(string="",required=True)
    first_name = fields.Char(string="",required=True)
    last_name = fields.Char(string="",required=True)
    picture = fields.Image(string="", required=False)
    current_mileage = fields.Float(string="",required=False)
    license_plate = fields.Char(string="",required=False)
    certificate_title= fields.Binary()
    register_date= fields.Date(string="YYYY-MM-DD",required=False)

    _sql_constrains = [
        ('vin', 'UNIQUE(vin)', 'You must to enter a valid vin')
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
            # match = re.search(r'[A-Z]\d4, [0-9]\d8, [0-9]\d2 | [A-Z]\d2', record)
            # if not match:
            if not record == 'hola':
                raise ValidationError("Must enter a valid vin")
        return super().create(record)

    @api.constrains('license_plate')
    def _check_vin(self):
        for record in self:
            # match = re.search(r'[A-Z]\d4, [0-9]\d8, [0-9]\d2 | [A-Z]\d2', record)
            # if not match:
            if record == '':
                raise ValidationError("Must enter a valid license_plate")
        return super().create(record)


   

#     vin - char, required
# first_name - char, required
# last_name - char, required
# picture - image
# current_mileage - float
# license_plate - char
# certificate_title - binary
# register_date - date