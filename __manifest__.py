# -*- coding: utf-8 -*-
{
    'name': "bookdatabase",

    'summary': """
        Manage a book database for a shop club""",

    'description': """
        Manage a book database for a shop club
    """,

    'author': "Mikel López",
    'website': "https://ioc.xtec.cat/educacio/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_users_views.xml',
        'report/book_report.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
