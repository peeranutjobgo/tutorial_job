from odoo import fields , models
 
class equipment_list(models.Model):
    _name = "equipment.request.list" 
    _description = "equipment list"

    name = fields.Char(required=True)
    quantity = fields.Float(default=1)
    
    quantity_unit = fields.Selection(
        string='unit',
        selection=[
            ('ptc','ptc'),
            ('ml', 'ml')
            ],
        default='ptc'
    )
    
    request_ids = fields.Many2one("equipment.request", required=True )
    