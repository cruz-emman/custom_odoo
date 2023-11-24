from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('Male','Male'),
('Female','Female')],string="Gender")
    