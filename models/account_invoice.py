from odoo import models, fields, api, _
from odoo.exceptions import UserError
from num2words import num2words


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    satuan = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh',
              'delapan', 'sembilan', 'sepuluh', 'sebelas']
    so_date = fields.Date(string='PO Date')
    no_faktur_pajak = fields.Char(string='Faktur Pajak')
    tanggal_faktur_pajak = fields.Date(string='Tanggal Faktur Pajak')

    @api.onchange('partner_id')
    def _partner_id_onchange(self):
        if self.partner_id.default_invoice_note:
            self.comment = self.partner_id.default_invoice_note

    def terbilang_(self, n):
        if n >= 0 and n <= 11:
            hasil = [self.satuan[int(n)]]
        elif n >= 12 and n <= 19:
            hasil = self.terbilang_(n % 10) + ['belas']
        elif n >= 20 and n <= 99:
            hasil = self.terbilang_(
                n / 10) + ['puluh'] + self.terbilang_(n % 10)
        elif n >= 100 and n <= 199:
            hasil = ['seratus'] + self.terbilang_(n - 100)
        elif n >= 200 and n <= 999:
            hasil = self.terbilang_(n / 100) + \
                ['ratus'] + self.terbilang_(n % 100)
        elif n >= 1000 and n <= 1999:
            hasil = ['seribu'] + self.terbilang_(n - 1000)
        elif n >= 2000 and n <= 999999:
            hasil = self.terbilang_(n / 1000) + \
                ['ribu'] + self.terbilang_(n % 1000)
        elif n >= 1000000 and n <= 999999999:
            hasil = self.terbilang_(n / 1000000) + \
                ['juta'] + self.terbilang_(n % 1000000)
        else:
            hasil = self.terbilang_(n / 1000000000) + \
                ['milyar'] + self.terbilang_(n % 100000000)
        return hasil

    def get_terbilang(self, bilangan):
        # num = abs(bilangan)
        # terbilang = ""
        # t = self.terbilang_(num)
        # while '' in t:
        #     t.remove('')
        # terbilang = ' '.join(t)
        # return terbilang
        res = num2words(bilangan, lang="id")
        return res.replace("koma nol", "") + " "

    @api.multi
    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        self.ensure_one()
        self.sent = True
        # return self.env['report'].get_action(self, 'account.report_invoice')
        return self.env['report'].get_action(self, 'gekha_mod.gekha_account_invoice_report_template')

    @api.multi
    def action_invoice_open(self):
        result = super(AccountInvoice, self).action_invoice_open()

        # get do_date
        if self.type == 'out_invoice' and self.name:
            origin_so = self.env['sale.order'].search(
                [('client_order_ref', '=', self.name)])
            self.so_date = origin_so.date_order

        return result

    def action_view_payments(self):

        action = self.env.ref(
            'account.action_account_payments').read()[0]
        action['domain'] = [('id', 'in', self.payment_ids.ids)]
        return action

        # return {
        #     'name': 'Payments',
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'tree',
        #     'view_mode': 'tree,form',
        #     'res_model': 'account.payment',
        #     'domain': [('id', 'in', self.payment_ids.ids)],
        # }
