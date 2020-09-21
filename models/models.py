# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.modules.module import get_module_resource
import base64
from dateutil.relativedelta import *
from datetime import date


class Book(models.Model):
    _name = 'bookdatabase.book'
    _description = 'Database\'s books'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('bookdatabase', 'static/src/img', 'default_book.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(size=32, string='Book\'s name', index=True)
    date_publish = fields.Date('Publish date')
    cover = fields.Image(default=_default_image)
    author_id = fields.Many2one('bookdatabase.author','Author')
    publisher_id = fields.Many2one('bookdatabase.publisher','Publisher')
    description = fields.Text()
    active = fields.Boolean('Active', default=True)
    creator_id = fields.Many2one('res.partner','Created by')
    comment_ids = fields.One2many('bookdatabase.comment','book_id','Comments')

class Author(models.Model):
    _name = 'bookdatabase.author'
    _description = 'Database\'s authors'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('bookdatabase', 'static/src/img', 'default_writer.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(size=32, string='Author\'s name')
    last_name = fields.Char(size=32, string='Author\'s last name', index=True)
    birthdate = fields.Date('Birthdate')
    deceasedate = fields.Date('Decease date')
    age = fields.Integer('Age', compute='_age_compute', readonly=True)
    book_ids = fields.One2many('bookdatabase.book','author_id','Books')

    @api.depends('birthdate')
    def _age_compute(self):
        today = date.today()
        for record in self:
            if not record.deceasedate:
                record.age = relativedelta(today, record.birthdate).years
            else:
                record.age = None

class Publisher(models.Model):
    _name = 'bookdatabase.publisher'
    _description = 'Database\'s publishers'

    name = fields.Char(size=32, string='Publisher\'s name')
    book_ids = fields.One2many('bookdatabase.book','publisher_id','Books')
    description = fields.Text()

class Comment(models.Model):
    _name = 'bookdatabase.comment'
    _order = 'datetime_publish'

    name = fields.Char(size=32, string="Subject")
    datetime_publish = fields.Datetime('Publish date')
    book_id = fields.Many2one('bookdatabase.book','Book')
    creator_id = fields.Many2one('res.partner','Created by')
    description = fields.Text()
    active = fields.Boolean('Active', default=True)