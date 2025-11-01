# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PropertyType(models.Model):
    """
    Property Type Model
    -------------------
    This model represents different types of properties (e.g., House, Apartment, Commercial).
    This is a simple model used to demonstrate Many2one relationships.
    """
    _name = 'property.type'
    _description = 'Property Type'
    _order = 'name'

    name = fields.Char(string='Type Name', required=True, help='Name of the property type')
    description = fields.Text(string='Description', help='Description of this property type')
    
    # Many2one field - properties that belong to this type
    # This creates a reverse One2many relationship in real.estate.property
    property_ids = fields.One2many('real.estate.property', 'property_type_id', string='Properties')
    property_count = fields.Integer(string='Property Count', compute='_compute_property_count')

    @api.depends('property_ids')
    def _compute_property_count(self):
        """Compute the number of properties for each type"""
        for record in self:
            record.property_count = len(record.property_ids)

