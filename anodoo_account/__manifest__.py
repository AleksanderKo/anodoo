# -*- coding: utf-8 -*-
{
    'name': "会计",

    'summary': """
        会计，财务等，是销售管理的基础模块
    """,

    'description': """
        会计，财务等，是销售管理的基础模块
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-account",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'account',

        'l10n_cn_small_business',
        'l10n_cn_standard',
    ],

    # always loaded
    'data': [
        'data/account_data.xml',
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/account_views.xml',
        'views/account_menu.xml',
        'views/account_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/account_demo.xml',
    ],
}