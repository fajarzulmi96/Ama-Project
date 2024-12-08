# -*- coding: utf-8 -*-
{
    'name': "AMA Module",

    'summary': """
        Anugerah Mortar Abadi Module Addons Custom
    """,

    'description': """
        Anugerah Mortar Abadi design print out for any module 
    """,

    'author': "Fajar Zulmi Sopian",
    'website': "",

    'category': 'Ama apps',
    'sequence': -100,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr_expense',
        'hr_contract', 
        'account',
        'mail',
        'mrp',
        'sale',
        'stock',
        'product',
        'contacts',
        'resource', 
    ],
    # 'base_setup', 'product', 'analytic', 'portal', 'digest'
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'view/ama_view.xml',
    ], 
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license':'LGPL-3',
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
