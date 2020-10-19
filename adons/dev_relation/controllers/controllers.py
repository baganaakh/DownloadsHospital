# -*- coding: utf-8 -*-
# from odoo import http


# class DevRelation(http.Controller):
#     @http.route('/dev_relation/dev_relation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_relation/dev_relation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_relation.listing', {
#             'root': '/dev_relation/dev_relation',
#             'objects': http.request.env['dev_relation.dev_relation'].search([]),
#         })

#     @http.route('/dev_relation/dev_relation/objects/<model("dev_relation.dev_relation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_relation.object', {
#             'object': obj
#         })
