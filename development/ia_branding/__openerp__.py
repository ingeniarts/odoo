# -*- coding: utf-8 -*-
{
    'auto_install': False,
    'installable': True,
    'name': "ia_branding",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "",
    'website': "",

    # Categories
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/ia_branding_web_layout.xml',
        'views/ia_branding_web_layout_secondary.xml',
        'views/ia_branding_web_login_layout.xml',
        #'views/ia_branding_logo.xml',
    ],
     'qweb': [
        'static/src/xml/ia_branding_base.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}