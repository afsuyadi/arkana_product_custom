# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Expenses(models.Model):
    _inherit = "product.product"
    
    employee_ids = fields.Many2many('hr.employee', string='Employee')
    is_ceiling = fields.Boolean('is Ceiling', default=False, required=True)
    ceiling_value = fields.Monetary('Value', required=True)
    
    
    
