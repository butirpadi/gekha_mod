from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vendor_reference = fields.Char(string='Vendor Reference')

    