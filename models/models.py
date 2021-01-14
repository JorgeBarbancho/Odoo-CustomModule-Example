# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.modules.module import get_module_resource
import base64
from dateutil.relativedelta import *
from datetime import date, datetime


class Book(models.Model):
    _name = 'bookdatabase.book'
    _description = 'Database\'s books'
    _order = 'date_publish'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('bookdatabase', 'static/src/img', 'default_book.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(size=32, string='Book\'s name',required=True, index=True)
    date_publish = fields.Date('Publish date')
    cover = fields.Image(default=_default_image)
    author_id = fields.Many2one('bookdatabase.author','Author')
    publisher_id = fields.Many2one('bookdatabase.publisher','Publisher')
    description = fields.Text()
    active = fields.Boolean('Active', default=True)
    creator_id = fields.Many2one('res.users','Created by',default=lambda self: self.env.user)
    comment_ids = fields.One2many('bookdatabase.comment','book_id','Comments')
    create_date = fields.Datetime('Create Date', default=datetime.now())

class Author(models.Model):
    _name = 'bookdatabase.author'
    _description = 'Database\'s authors'
    _order = 'last_name'
    _inherit = ['image.mixin']

    @api.model
    def _default_image(self):
        image_path = get_module_resource('bookdatabase', 'static/src/img', 'default_writer.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(size=32, string='Author\'s name',required=True)
    last_name = fields.Char(size=32, string='Author\'s last name', required=True, index=True)
    image = fields.Image(default=_default_image)
    birthdate = fields.Date('Birthdate')
    is_dead = fields.Boolean('Is dead?')
    deceasedate = fields.Date('Decease date')
    age = fields.Integer('Age', compute='_age_compute', readonly=True)
    book_ids = fields.One2many('bookdatabase.book','author_id','Books')

    @api.depends('birthdate','is_dead','birthdate')
    def _age_compute(self):
        today = date.today()
        for record in self:
            if not record.is_dead:
                record.age = relativedelta(today, record.birthdate).years
            else:
                record.age = None

    def name_get(self):
        result = []
        for record in self:
            name = record.name + ' ' + record.last_name
            result.append((record.id, name))
        return result

class Publisher(models.Model):
    _name = 'bookdatabase.publisher'
    _description = 'Database\'s publishers'

    name = fields.Char(size=32, string='Publisher\'s name')
    book_ids = fields.One2many('bookdatabase.book','publisher_id','Books')
    description = fields.Text()

class Comment(models.Model):
    _name = 'bookdatabase.comment'
    _order = 'datetime_publish'

    @api.model
    def _myself(self):
        return self.env.user

    @api.model
    def _book(self):
        libro=self.env.context.get('book_id')
        return libro

    name = fields.Char(size=32, string="Subject")
    datetime_publish = fields.Datetime('Publish date', default=datetime.now())
    book_id = fields.Many2one('bookdatabase.book','Book', default=_book)
    creator_id = fields.Many2one('res.users','Created by', default=_myself)
    description = fields.Text()
    active = fields.Boolean('Active', default=True)