from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResCompany(models.Model):
    _inherit = 'res.company'

    report_validated_by = fields.Char(string='Validated by')
    report_verified_by = fields.Char(string='Verified by')
    report_approved_by = fields.Char(string='Approved by')
    
    invoice_footer_note = fields.Text(
        string='Invoice Footer Note',
    )

    purchase_note = fields.Text(string='Default Purchase Terms & Conditions')
    kwitansi_logo = fields.Binary(string='Logo Kwitansi')
    