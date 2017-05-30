# picture_gallery_master.py
# -*- coding: utf-8 -*-

from openerp import models, fields, api, tools

_logger = logging.getLogger(__name__)

# Table messages
class messages(models.Model):
    _name = 'eai_server.messages'
    _descrition = 'EAI Server Messages'
    
    create_date = fields.datetime('Creation Date', required=True)
    direction = fields.selection([
       ('outgoing', 'Outgoing Message'),
       ('incoming', 'Incoming Message'),
       ]'Direction', required=True) 
    name = fields.Char('Name')
    sender_id = fields.many2one('res.partner', string='Sender', required=True)
    receiver_id = fields.many2one('res.partner', string='Receiver', required=True)
    state = fields.selection([
       ('created', 'Message Created'),
       ('mapping_ok', 'Message Mapping OK'),
       ('mapping_nok', 'Message Mapping Failed'),
       ('sent', 'Message Sent'),
       ('sent_ok', 'Message Sent OK'),
       ('sent_nok', 'Message Sent Failed'),
       ('cancel', 'Message Manually Cancelled'),
       ('delected', 'Message Manually Deleted'),
       ('waiting', 'Message Waiting Schedule'),
       ('progress', 'Message in Progress'),
       ], 'Status') 
    
