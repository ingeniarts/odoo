# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'ia_base',
    'version': '1.3',
    'category': 'Uncategorized',
    'description': """Chargement des informations de base pour Ingeniarts""",
    'author': 'François Lefebvre',
    'maintainer': 'Louis-Pierre T. Létourneau',
    'website': '',
    'depends': ["base", "l10n_ca", "l10n_ca_toponyms"],
    'data': [
        'ia_base_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}