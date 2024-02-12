from odoo import fields , models , api
 
class equ_request_approve(models.Model):
    _name = "equipment.request.approve" 
    _description = "equipment list"

    req_approver_name = fields.Char(required=True)
    req_approve_1 = fields.Boolean() 
    # req_approve_2 = fields.Boolean()
    req_state = fields.Selection(
        string='state',
        selection=[('approve','approve'),('reject', 'reject')],
        default='New request',
        required=True
    )
    req_id = fields.Many2one("equipment.request", required=True )

    def change_state_to_reject(self):
        for record in self:
            record.req_approve_1 = False
            record.req_approve_2 = False
            record.req_state = "reject"
        return True
    
    def change_approve(self):
        for record in self:
            record.req_approve_1 = True
        return True

