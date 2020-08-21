# -*- coding: utf-8 -*-
from odoo import http

# class GekhaMod(http.Controller):
#     @http.route('/gekha_mod/gekha_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gekha_mod/gekha_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gekha_mod.listing', {
#             'root': '/gekha_mod/gekha_mod',
#             'objects': http.request.env['gekha_mod.gekha_mod'].search([]),
#         })

#     @http.route('/gekha_mod/gekha_mod/objects/<model("gekha_mod.gekha_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gekha_mod.object', {
#             'object': obj
#         })