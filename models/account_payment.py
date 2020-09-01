from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    receipt_note = fields.Text(string='Receipt Note')
    satuan = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh',
              'delapan', 'sembilan', 'sepuluh', 'sebelas']
    terbilang = fields.Char(string='Terbilang', compute='_compute_terbilang', store=True)

    @api.depends('state')
    def _compute_terbilang(self):
        for rec in self:
            if rec.state == 'posted':
                rec.terbilang = rec.get_terbilang(rec.amount)

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
        num = abs(bilangan)
        terbilang = ""
        t = self.terbilang_(num)
        while '' in t:
            t.remove('')
        terbilang = ' '.join(t)
        return terbilang

    def action_print_receipt(self):
        action = self.env.ref(
            'gekha_mod.gekha_account_payment_receipt_action').read()[0]
        return action
