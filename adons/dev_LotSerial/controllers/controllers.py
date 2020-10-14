# -*- coding: utf-8 -*-
# from odoo import http


# class DevStar(http.Controller):
#     @http.route('/dev_star/dev_star/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_star/dev_star/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_star.listing', {
#             'root': '/dev_star/dev_star',
#             'objects': http.request.env['dev_star.dev_star'].search([]),
#         })

#     @http.route('/dev_star/dev_star/objects/<model("dev_star.dev_star"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_star.object', {
#             'object': obj
#         })
