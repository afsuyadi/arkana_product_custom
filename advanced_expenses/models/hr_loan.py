# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Loan(models.Model):
    _inherit = "hr.loan"
    
    expense_id = fields.Many2one('hr.expense', string='HR Expenses', domain="[('is_loan', '=', True),('employee_id', '=', employee_id)]")
    
    @api.constrains('employee_id')
    def _retrieve_loan_value(self):
        for rec in self :
            difference = rec._get_difference_value()
            if difference :
                rec.amount = difference
            else :
                rec.amount = 0

    def _get_difference_value(self):
        difference = self.env['hr.expense'].search([('employee_id', '=', self.employee_id.id),
                                                       ('product_id', '=', self.product_id.id),                                                       
                                                       ], limit=1)
        return difference