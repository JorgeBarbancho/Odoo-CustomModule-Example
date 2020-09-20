# -*- coding: utf-8 -*-
# from odoo import http


# class Bookdatabase(http.Controller):
#     @http.route('/bookdatabase/bookdatabase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookdatabase/bookdatabase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookdatabase.listing', {
#             'root': '/bookdatabase/bookdatabase',
#             'objects': http.request.env['bookdatabase.bookdatabase'].search([]),
#         })

#     @http.route('/bookdatabase/bookdatabase/objects/<model("bookdatabase.bookdatabase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookdatabase.object', {
#             'object': obj
#         })
