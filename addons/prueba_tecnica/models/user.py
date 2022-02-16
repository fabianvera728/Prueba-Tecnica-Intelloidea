from odoo import api, fields, models, _

class TecnicaUser(models.Model):
    # _name = "prueba.users"
    _inherit = ["res.users"]
    res_name="prueba.testuser"
    res_description="Prueba tecnica usuario"

    # name = fields.Char(string="Prueba usuario", required=True, translate=True)
    # age = fields.Char(string="Edad")
    # nit = fields.Char(string="Nit")
    # email = fields.Char(string="Email")

    @api.model
    def create(self, vals):
        return super(TecnicaUser, self).create(vals)
