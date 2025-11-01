# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version': '18.0.0.0.2',
    'category': 'Sales',
    'summary': 'Real Estate Management Module - Training Example',
    'description': """
Real Estate Management
=====================
This module is a training example that demonstrates how to build Odoo apps.

Features:
---------
* Property Management
* Property Types (Many2one relationship)
* Property Tags (Many2many relationship)
* List, Form, and Search Views
* Security and Access Rights

This module showcases:
* Model creation with various field types
* Many2one relationships
* Many2many relationships
* View creation (list, form, search)
* Security configuration
    """,
    'author': 'Training Example',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_type_views.xml',
        'views/property_tag_views.xml',
        'views/property_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

