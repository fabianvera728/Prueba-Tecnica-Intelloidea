from odoo import api, fields, models

class TecnicaProduct(models.Model):
    # _name="prueba.product"
    _inherit=["product.product"]
    product_name ="prueba.product"
    # _description="Prueba tecnica producto"

    # name = fields.Char(string="Prueba producto", required=True, translate=True)
    # note = fields.Text(string="Descripcion")

    @api.model
    def create(self, vals):
        return super(TecnicaProduct, self).create(vals)