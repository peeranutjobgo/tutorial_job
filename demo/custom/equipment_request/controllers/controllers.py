# -*- coding: utf-8 -*-
# from odoo import http


# class EquipmentRequest(http.Controller):
#     @http.route('/equipment_request/equipment_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/equipment_request/equipment_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('equipment_request.listing', {
#             'root': '/equipment_request/equipment_request',
#             'objects': http.request.env['equipment_request.equipment_request'].search([]),
#         })

#     @http.route('/equipment_request/equipment_request/objects/<model("equipment_request.equipment_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('equipment_request.object', {
#             'object': obj
#         })

