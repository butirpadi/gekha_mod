from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        self.ensure_one()
        self.sent = True
        # return self.env['report'].get_action(self, 'account.report_invoice')
        return self.env['report'].get_action(self, 'gekha_mod.gekha_account_invoice_report_template')

    