# -*- coding: utf-8 -*-
{
    'name': "advanced_expenses",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "PT Arkana Solusi Digital",
    'website': "https://www.arkana.co.id",
    'category': 'Uncategorized',
    'version': '17.1',
    'depends': ['base', 'hr_expense', 'product', 'hr', 'loan_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/expense_categories.xml',
        'views/hr_expense_views.xml',
        'views/hr_loan_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
