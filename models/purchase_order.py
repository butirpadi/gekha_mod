from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def _default_purchase_note(self):
        return self.env.user.company_id.purchase_note
        
    notes = fields.Text('Terms and Conditions', default=_default_purchase_note)

