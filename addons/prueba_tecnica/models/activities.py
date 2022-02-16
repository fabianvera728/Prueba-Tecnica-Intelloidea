from odoo import api, fields, models, _

class TodoTask(models.Model):
    _inherit = ['project.task']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')