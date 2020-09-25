# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class Users(models.Model):

    _inherit = "res.users"

    comment_ids = fields.One2many('bookdatabase.comment','creator_id','Comments')