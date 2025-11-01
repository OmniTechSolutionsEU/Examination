# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PropertyTag(models.Model):
    """
    Property Tag Model
    ------------------
    This model represents tags that can be assigned to properties.
    This demonstrates Many2many relationships.
    """
    _name = 'property.tag'
    _description = 'Property Tag'
    _order = 'name'

    name = fields.Char(string='Tag Name', required=True, help='Name of the tag')
    color = fields.Integer(string='Color', default=0, help='Color used for the tag')
    description = fields.Text(string='Description', help='Description of this tag')
    
    # Many2many relationship - properties that have this tag
    # This creates a bidirectional many2many relationship
    property_ids = fields.Many2many('real.estate.property', 'property_tag_rel', 
                                    'tag_id', 'property_id', string='Properties')

