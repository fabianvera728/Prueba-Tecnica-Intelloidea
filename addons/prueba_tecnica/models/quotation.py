from odoo import api, fields, models, _

class TecnicaQuotation(models.Model):
    _inherit = ['sale.order']
    sale_name="prueba.quotation"
    sale_description = fields.Char(string="Contacto del usuario")
    sale_contact = fields.Many2one(
        comodel_name='prueba.contact',
        string="Contacto del usuario",
        required=True,
        tracking=True
    )
    # prueba_tecnica.field_sale_order__sale_contact