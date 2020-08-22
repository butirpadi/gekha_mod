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
    'depends': ['base','stock','purchase','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_format.xml',
        'reports/gekha_sales_report.xml',
        'reports/gekha_purchase_order_print.xml',
        'reports/stock_picking_report.xml',
        'views/gekha_view_order_form.xml',
        'views/purchase_order_form.xml',
        'views/res_company_view.xml',
        'views/stock_picking_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}