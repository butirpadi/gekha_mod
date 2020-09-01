from odoo import fields, models, api, _
from odoo.exceptions import UserError
from pprint import pprint


class WizardTaxReportDetail(models.TransientModel):
    _name = 'wizard.tax.report.detail'

    wizard_id = fields.Many2one('wizard.tax.report', string='Wizard')
    tax_type = fields.Selection(
        [("sale", "PPN Keluaran"), ("purchase", "PPN Masukan")], string='Payment Method')
    invoice_id = fields.Many2one('account.invoice', string='Invoice')
    date_invoice = fields.Date('Date Invoice')
    partner_id = fields.Many2one('res.partner', string='Partner')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Integer('Quantity')
    dpp = fields.Float('DPP')
    ppn = fields.Float('PPN 10%')
    total = fields.Float('DPP + PPN 10%')
