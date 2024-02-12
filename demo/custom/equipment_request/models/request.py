from odoo import fields , models ,api
from datetime import datetime, timedelta

class request(models.Model):
    _name = "equipment.request" 
    _description = "show equipment request list"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']


    # basic fields and modify fields (required, default, string, selection, readonly)
    name = fields.Char(required=True)
    description = fields.Text(string='Objective of request')
    day_of_availability = fields.Integer(default='3', required=True)
    day_of_return = fields.Integer(required=True)
    urgent_case = fields.Boolean()
    delay_case = fields.Boolean()
    department = fields.Selection(
        string='Department',
        selection=[
            ('IT', 'IT'),
            ('marketing', 'marketing'),
            ('operation', 'operation'),
            ('finance', 'finance')
        ],
        required =True 
    )
    
    state = fields.Selection(
        string='state',
        selection=[
            ('new_request','New request'),
            ('paining', 'Paining'),
            ('received','Received'),
            ('return','Return'),
            ('canceled','Canceled')],
        default='new_request' ,
        required =True 
    )
    
    # many2one many2many one2many
    # tag_ids = fields.Many2many("equipment.request.tag", string="tag")
    equipment_list_ids = fields.One2many("equipment.request.list", "request_ids", string="Equipment List")
    
    # compute fields
    date_of_received = fields.Date(
            compute="_compute_date_of_received" , 
            readonly = True)
    date_of_return = fields.Date(
            compute="_compute_date_of_return",
            readonly = True)
    
    @api.depends('day_of_availability')
    def _compute_date_of_received(self):
        for record in self:
            record.date_of_received = datetime.today() + timedelta(days= record.day_of_availability)

    @api.depends('day_of_return')
    def _compute_date_of_return(self):
        for record in self:
            record.date_of_return = record.date_of_received + timedelta(days= record.day_of_return)
    
    # onchange
    @api.onchange("req_urgent_case")
    def _onchange_urgent_case(self):
        self.day_of_availability = 1 

    # some action
    def change_state_to_canceled(self):
        for record in self:
            record.state = "canceled"
        return True
    
    # approve request
    # approve_id = fields.One2many("equipment.request.approve", "req_id", string="approve list")
    def change_state_to_received(self):
        for record in self:
            record.state = "received"
        return True
    
    # return request
    def change_state_to_return(self):
        for record in self:
            record.state = "return"
        return True