# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class RealEstateProperty(models.Model):
    """
    Real Estate Property Model
    ---------------------------
    Main model for managing real estate properties.
    This model demonstrates:
    - Basic field types (Char, Text, Float, Integer, Date, Boolean)
    - Many2one relationships (property_type_id)
    - Many2many relationships (tag_ids)
    - Computed fields
    - Default values
    - Constraints
    """
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    _order = 'name'

    # Basic Information Fields
    name = fields.Char(string='Property Name', required=True, help='Name of the property')
    description = fields.Text(string='Description', help='Detailed description of the property')
    postcode = fields.Char(string='Postcode', help='Postal code of the property location')
    date_availability = fields.Date(string='Available From', 
                                    default=lambda self: fields.Date.today() + timedelta(days=90),
                                    help='Date when the property will be available')
    
    # Numeric Fields
    expected_price = fields.Float(string='Expected Price', required=True, 
                                 digits=(16, 2), help='Expected selling price')
    selling_price = fields.Float(string='Selling Price', readonly=True, 
                                digits=(16, 2), help='Actual selling price')
    best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer',
                             help='Best offer received for this property')
    
    # Numeric Fields - Dimensions
    bedrooms = fields.Integer(string='Bedrooms', default=2, help='Number of bedrooms')
    living_area = fields.Float(string='Living Area (sqm)', help='Living area in square meters')
    facades = fields.Integer(string='Facades', help='Number of facades')
    garage = fields.Boolean(string='Garage', default=False, help='Has garage')
    garden = fields.Boolean(string='Garden', default=False, help='Has garden')
    garden_area = fields.Float(string='Garden Area (sqm)', help='Garden area in square meters')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], string='Garden Orientation', help='Orientation of the garden')
    
    # Status Fields
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='Status', default='new', required=True, help='Current status of the property')
    
    # Relational Fields
    # Many2one: Each property belongs to one property type
    property_type_id = fields.Many2one('property.type', string='Property Type',
                                       help='Type of property (e.g., House, Apartment)')
    
    # Many2many: Each property can have multiple tags
    tag_ids = fields.Many2many('property.tag', 'property_tag_rel', 
                              'property_id', 'tag_id', string='Tags',
                              help='Tags associated with this property')
    
    # Many2one to res.users (salesperson)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', 
                                    default=lambda self: self.env.user,
                                    help='Salesperson responsible for this property')
    
    # Many2one to res.partner (buyer)
    buyer_id = fields.Many2one('res.partner', string='Buyer', 
                              readonly=True, help='Buyer of the property')
    
    # Computed Fields
    total_area = fields.Float(string='Total Area (sqm)', compute='_compute_total_area',
                             help='Total area (living area + garden area)')
    
    # Offer count (to demonstrate computed fields)
    offer_count = fields.Integer(string='Offer Count', compute='_compute_offer_count')
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        """Compute total area from living area and garden area"""
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends('expected_price')
    def _compute_best_offer(self):
        """Compute best offer (placeholder - in real app would compute from offers)"""
        for record in self:
            # In a real application, this would query actual offers
            record.best_offer = 0.0
    
    @api.depends('state')
    def _compute_offer_count(self):
        """Compute number of offers (placeholder)"""
        for record in self:
            # In a real application, this would count actual offers
            record.offer_count = 0
    
    # Constraints
    @api.constrains('expected_price', 'selling_price')
    def _check_prices(self):
        """Ensure selling price is positive"""
        for record in self:
            if record.expected_price <= 0:
                raise ValueError('Expected price must be positive!')
            if record.selling_price and record.selling_price <= 0:
                raise ValueError('Selling price must be positive!')
    
    # Actions
    def action_sold(self):
        """Mark property as sold"""
        for record in self:
            if record.state == 'canceled':
                raise ValueError('Cannot sell a canceled property!')
            record.state = 'sold'
    
    def action_cancel(self):
        """Mark property as canceled"""
        for record in self:
            if record.state == 'sold':
                raise ValueError('Cannot cancel a sold property!')
            record.state = 'canceled'

