from odoo import fields, models

class Motorcycle(models.Model):
    _name = "motorcycle.course"
    _description = "Course Info two"
    _rec_name="registry_number"
    registry_number = fields.Char(string = "Name", required=True)
    vin = fields.Char(string="",required=True)
    first_name = fields.Char(string="",required=True)
    last_name = fields.Char(string="",required=True)
    picture = fields.Image(string="", required=False)
    current_mileage = fields.Float(string="",required=False)
    license_plate = fields.Char(string="",required=False)
    certificate_title= fields.Binary(string="",required=False)
    register_date= fields.Date(string="YYYY-MM-DD",required=False)
#     vin - char, required
# first_name - char, required
# last_name - char, required
# picture - image
# current_mileage - float
# license_plate - char
# certificate_title - binary
# register_date - date