from odoo import models, fields, api


class DocumentDateRange(models.TransientModel):
    _name = 'documents_module.document.date_range'
    _description = 'Dokumentų Filtravimo Forma'

    start_date = fields.Date(string='Nuo datos', required=True)
    end_date = fields.Date(string='Iki datos', required=True)

    def print_document_list(self):
        documents = self.env['documents_module.document'].search([
            ('date', '>=', self.start_date),
            ('date', '<=', self.end_date)
        ])
        for document in documents:
            print(document.name)
