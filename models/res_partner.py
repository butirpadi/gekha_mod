from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    npwp = fields.Char('NPWP')
    default_invoice_note = fields.Text('Default Note')
