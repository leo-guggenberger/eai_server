# picture_gallery_master.py
# -*- coding: utf-8 -*-

from openerp import models, fields, api, tools

_logger = logging.getLogger(__name__)

# Table messages
class messages(models.Model):
    _name = 'eai_server.messages'
    _descrition = 'EAI Server Messages'
    
    date = fields.Date('Date', required=True)
    time = fields.Time('Time', required=True)
    direction = fields.Char('Direction', required=True) 
    sender = fields.Char('Sender', required=True)
    receiver = fields.Char('Receiver', required=True)
    status = fields.Char('Status')
    
    @api.one
