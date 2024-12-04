from odoo import models, fields

class LibraryGenre(models.Model):
    _name = 'library.genre'
    _description = 'Book Genre'

    name = fields.Char(string='Genre', required=True)

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    page_count = fields.Integer(string='Page Count')
    genre_ids = fields.Many2many('library.genre', string='Genres')
