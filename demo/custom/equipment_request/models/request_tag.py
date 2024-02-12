from odoo import fields , models;


class equipment_request_tag(models.Model):
    _name = "equipment.request.tag" 
    _description = "equipment request tag"

    name = fields.Char(required=True)
