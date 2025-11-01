# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):

    _inherit = 'res.partner'

    real_estate_property_id = fields.Many2one(comodel_name="real.estate.property", string="Real Estate Property")