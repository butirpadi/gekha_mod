# -*- coding: utf-8 -*-
{
    'name': "PT Gekha Karunia Abadi Mod",

    'summary': """
        Custom module for PT Gekha Karunia Abadi""",

    'description': """
        Custom module for PT Gekha Karunia Abadi
    """,

    'author': "butirpadi@gmail.com",
    'website': "http://www.github.com/butirpadi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','purchase','sale','account','account_cancel'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_format.xml',
        'reports/report_layout.xml',
        'reports/gekha_sales_report.xml',
        'reports/gekha_purchase_order_print.xml',
        'reports/stock_picking_report.xml',
        'reports/stock_picking_report.xml',
        'reports/account_invoice_report.xml',
        'reports/journal_entry_report.xml',
        'reports/ar_ap_report.xml',
        'views/gekha_view_order_form.xml',
        'views/purchase_order_form.xml',
        'views/res_company_view.xml',
        'views/stock_picking_view.xml',
        'views/invoice_form_view.xml',
        'views/view_account_journal_form.xml',
        'views/wizard_journal_entry_report.xml',
        'views/wizard_ar_ap_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}