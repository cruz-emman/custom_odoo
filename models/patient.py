from odoo import models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit ="mail.thread"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age")
    gender = fields.Selection([("Male", "Male"), ("Female", "Female")], string="Gender")
    active = fields.Boolean(string="Active")
