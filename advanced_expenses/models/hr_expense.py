# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HREmployee(models.Model):
    _inherit = "hr.expense"
    
    difference = fields.Monetary('Loan Amount')
    is_loan = fields.Boolean('Employee Loan', default=False)
    
    @api.onchange('employee_id', 'total_amount_currency', 'product_id')
    def _count_expense_difference(self):
        for rec in self :
            ceiling_value = rec._get_ceiling_value_record()
            if not ceiling_value:
                rec.difference = 0
            else:
                difference = rec.total_amount_currency - ceiling_value.ceiling_value
                if difference > 0 :
                    rec.difference = difference
                    rec.is_loan = True
                    # print(rec.is_loan)
                else:
                    rec.difference = 0
                    rec.is_loan = False
                    
    def _get_ceiling_value_record(self):
        record = self.env['product.product'].search([
                    ('is_ceiling', '=', True), 
                    ('ceiling_value', '>', 0),
                    ('employee_ids', 'in', self.employee_id.id),
                    ('id', '=', self.product_id.id)],limit=1)
        return record
                    
    
    
                    

    
    