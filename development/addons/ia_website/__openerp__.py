# -*- coding: utf-8 -*-
{
    'auto_install': False,
    'installable': True,
    'name': "ia_website",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "LP",
    'website': "http://www.ingeniarts.com",

    # Categories
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'purchase', 'sale', 'website_form','website_partner', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/ia_website_footer.xml',
        'views/ia_website_autofooter.xml',
    ],
     #'qweb': [
     #   'static/src/xml/ia_website.xml',
    #],
    # only loaded in demonstration mode
}