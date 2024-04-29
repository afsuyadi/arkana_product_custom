# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class advanced_expenses(models.Model):
#     _name = 'advanced_expenses.advanced_expenses'
#     _description = 'advanced_expenses.advanced_expenses'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class HRReimburse(models.Model):
    _inherit = "product.product"
    
    name = fields.Char('Name')
    is_plafon = fields.Boolean('Plafon')
    amount = fields.Integer('amount')
    plafon_value = fields.Integer('Cost')
