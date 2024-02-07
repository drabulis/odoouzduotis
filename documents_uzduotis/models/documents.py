from odoo import models, fields


class Document(models.Model):
    _name = 'documents_module.document'
    _description = 'Dokumentai'

    name = fields.Char(string='Pavadinimas', required=True)
    description = fields.Text(string='Aprašymas')
    company_id = fields.Many2one('res.company', string='Įmonė', required=True)
    date = fields.Date(string='Data', required=True)
