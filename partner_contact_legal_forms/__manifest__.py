# Copyright © 2018 Matteo Bilotta (Link IT s.r.l.)
#
# GNU Affero General Public License v3.0

# noinspection PyStatementEffect
{
    'name': "Contacts Legal Forms",
    'summary': """Adds "Legal form" field on company contacts.""",
    'description': """
        This module extends the standard Odoo's "res.partner"
        views adding "Legal form" field on company contacts.
    """,

    'author': "Link IT Srl",
    'website': "http://linkgroup.it/",

    'category': "Customer Relationship Management",
    'version': '11.0.1.0.0',

    'depends': ['base'],

    'data': [
        'data/res.partner.form.csv',
        'security/ir.model.access.csv',
        'views/res_partner.xml'
    ],
    'demo': [],
    'qweb': []
}
