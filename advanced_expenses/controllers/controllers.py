# -*- coding: utf-8 -*-
# from odoo import http


# class AdvancedExpenses(http.Controller):
#     @http.route('/advanced_expenses/advanced_expenses', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advanced_expenses/advanced_expenses/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('advanced_expenses.listing', {
#             'root': '/advanced_expenses/advanced_expenses',
#             'objects': http.request.env['advanced_expenses.advanced_expenses'].search([]),
#         })

#     @http.route('/advanced_expenses/advanced_expenses/objects/<model("advanced_expenses.advanced_expenses"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advanced_expenses.object', {
#             'object': obj
#         })
