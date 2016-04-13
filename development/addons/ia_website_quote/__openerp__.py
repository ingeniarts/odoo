# -*- coding: utf-8 -*-
{

    'installable': True,
    'auto_install': False,

    'name': "ia_website_quote",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "LP v0",
    'website': "http://www.ingeniarts.com",

    # Categories
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'purchase', 'sale', 'website_form','website_partner', 'crm', 'website_quote',
                'website', 'mail', 'web_tip', 'payment', 'website_portal_sale', 'website_mail'],



    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'views/ia_website_quote_pricing.xml',
        'views/ia_website_quote_content.xml',
        #'data/ia_website_quotation_data.xml',
        'views/ia_website_quote_quotation.xml',
    ],
     #'qweb': [
     #   'static/src/xml/ia_website.xml',
    #],
    # only loaded in demonstration mode
}