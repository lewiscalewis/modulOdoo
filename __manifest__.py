# -*- coding: utf-8 -*-
{
    'name': "fcties",

    'summary': """
        Modulo de la práctica final""",

    'description': """
        Módulo by Leví :P
    """,

    'author': "Levi Vicente Navarro",
    'website': "http://www.iesmurgi.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/informe.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
