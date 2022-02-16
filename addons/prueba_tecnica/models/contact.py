from odoo import api, fields, models, _

class TecnicaContact(models.Model):
    _name="prueba.contact"
    _description="Prueba tecnica Contacto"

    # name = fields.Char(string="Nombre", required=True, translate=True)
    name = fields.Many2one(
        comodel_name='res.users',
        string='Usuario',
        required=True,
        tracking=True
    )
    phone = fields.Char(string="Telefono", required=True, translate=True)
    address = fields.Char(string="Dirección", required=True, translate=True)
    email = fields.Char(string="Correo electronico", required=True, translate=True)

    note = fields.Text(string="Descripcion")

    @api.model
    def create(self, vals):
        return super(TecnicaContact, self).create(vals)