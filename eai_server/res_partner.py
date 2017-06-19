# res_partner.py
# -*- coding: utf-8 -*-

from odoo import api, fields, models

# Table inherit partner
class ResPartner(models.Model):
    _name = 'eai_server.res.partner'
    _inherit = 'res.partner'

    eai_client_ids = fields.One2many('eai_server.clients', 'client_id', 'ClientID')
