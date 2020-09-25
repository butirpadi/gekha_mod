from odoo import fields, models, api, _
from odoo.exceptions import UserError
from pprint import pprint


class WizardTaxReport(models.TransientModel):
    _name = 'wizard.tax.report'

    name = fields.Char(string="Name", default="Tax Report")
    date_from = fields.Date(string='Start Date', required=True, )
    date_to = fields.Date(string='End Date', required=True, )
    tax_type = fields.Selection([("sale", "PPN Keluaran"), ("purchase", "PPN Masukan"), (
        "sale_purchase", "PPN Keluaran & Masukan (Selisih)")], string='Tax Type', required=True, default="sale")

    report_line_ids = fields.One2many(
        comodel_name='wizard.tax.report.detail',
        inverse_name='wizard_id',
        string='Report Lines',
    )

    def get_digits(self, name):
        digit = self.env['decimal.precision'].search(
            [('name', '=', name)], limit=1)
        return digit.digits

    def process_wizard(self):
        ir_val = self.env['ir.values']

        if self.tax_type == 'purchase':
            tax_ids = ir_val.get_default(
                'product.template', 'supplier_taxes_id', company_id=self.env.user.company_id.id)
        elif self.tax_type == "sale":
            tax_ids = ir_val.get_default(
                'product.template', 'taxes_id', company_id=self.env.user.company_id.id)
        else:
            sale_tax_ids = ir_val.get_default(
                'product.template', 'taxes_id', company_id=self.env.user.company_id.id)
            purchase_tax_ids = ir_val.get_default(
                'product.template', 'supplier_taxes_id', company_id=self.env.user.company_id.id)

        if self.tax_type in ['sale', 'purchase']:
            default_tax = self.env['account.tax'].search(
                [('id', '=', tax_ids[0])])
        else:
            default_tax = self.env['account.tax'].search(
                ['|', ('id', '=', sale_tax_ids[0]), ('id', '=', purchase_tax_ids[0])])

        # Using Invoices
        if self.tax_type == 'sale':
            invoices = self.env['account.invoice'].search(
                ['&', '&', ('type', '=', 'out_invoice'), ('amount_tax', '>', 0), ('state', 'in', ['open', 'paid'])])
        elif self.tax_type == 'purchase':
            invoices = self.env['account.invoice'].search(
                ['&', '&', ('type', '=', 'in_invoice'), ('amount_tax', '>', 0), ('state', 'in', ['open', 'paid'])])
        else:
            invoices = self.env['account.invoice'].search(
                [('amount_tax', '>', 0), ('state', 'in', ['open', 'paid'])])

        if self.tax_type in ['sale', 'purchase']:
            report_detail = []
            for inv in invoices:
                for line in inv.invoice_line_ids:
                    if default_tax[0].id in line.invoice_line_tax_ids.ids:
                        dpp = 0
                        ppn = 0
                        total = 0

                        if default_tax[0].include_base_amount:
                            dpp = line.price_unit / \
                                (default_tax.amount / 100 + 1)
                            total = line.price_unit
                            ppn = total - dpp
                        else:
                            dpp = line.price_unit
                            ppn = default_tax.amount / 100 * dpp
                            total = dpp+ppn

                        report_detail.append(
                            (0, False, {
                                'tax_type': self.tax_type,
                                'invoice_id': inv.id,
                                'date_invoice': inv.date_invoice,
                                'partner_id': inv.partner_id.id,
                                'product_id': line.product_id.id,
                                'quantity': line.quantity,
                                'dpp': line.quantity * dpp,
                                'ppn': line.quantity * ppn,
                                'total': line.quantity * total,
                            })
                        )

            self.report_line_ids.unlink()
            self.report_line_ids = report_detail
        else:
            # all type tax report
            report_detail = []
            for inv in invoices:

                # get line with taxes
                # taxed_lines = inv.invoice_line_ids.filtered(
                #     lambda x: x.invoice_line_tax_ids.filtered(lambda y: y.id in default_tax.ids))

                print('Invoice Tax Lines')
                pprint(inv.tax_line_ids)

                inv_taxes = inv.tax_line_ids.filtered(
                    lambda x: x.tax_id.id in default_tax.ids)

                print('Filtered Tax Lines')
                pprint(inv_taxes)

                for tax in inv_taxes:
                    report_detail.append(
                        (0, False, {
                            'tax_type': tax.tax_id.type_tax_use,
                            'invoice_id': inv.id,
                            'date_invoice': inv.date_invoice,
                            'partner_id': inv.partner_id.id,
                            'dpp': tax.base,
                            'ppn': tax.amount,
                            'total': tax.base + tax.amount,
                        })
                    )

            self.report_line_ids.unlink()
            self.report_line_ids = report_detail

        # return self.env['report'].get_action(self, 'gekha_mod.gekha_tax_report_action')
        if self.tax_type in ['sale', 'purchase']:
            action = self.env.ref(
                'gekha_mod.gekha_ppn_report_action').read()[0]
            return action
        else:
            action = self.env.ref(
                'gekha_mod.gekha_ppn_difference_report_action').read()[0]
            return action
