from odoo import fields, models, api, _
from odoo.exceptions import UserError
from pprint import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta



class WizardArAp(models.TransientModel):

    _name = 'wizard.ar.ap'
    name = fields.Char(string='Name', default="AR/AP Report")
    period_date = fields.Date(string='Period Date', required=True)
    period_length = fields.Integer(string="Period Length (days)", defaullt=30)
    account_type = fields.Selection([("ar", "Receivable Accounts"), ("ap", "Payabel Accounts"), (
        "ar_ap", "Receivable and Payable Accounts")], string='Payment Method', default="ar", required=True)
    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='wizard_ar_ap_partner_rel',
        column1='wizard_id',
        column2='partner_id',
        string='Partners'
    )
    invoice_ids = fields.Many2many(
        comodel_name='account.invoice',
        relation='wizard_ar_ap_invoice_rel',
        column1='wizard_id',
        column2='invoice_id',
        string='Invoices'
    )
    # invoice_0_30 = fields.Many2many(
    #     comodel_name='account.invoice',
    #     relation='wizard_ar_ap_invoice_0_30_rel',
    #     column1='wizard_id',
    #     column2='invoice_id',
    #     string='Invoices'
    # )
    # invoice_30_60 = fields.Many2many(
    #     comodel_name='account.invoice',
    #     relation='wizard_ar_ap_invoice_30_60_rel',
    #     column1='wizard_id',
    #     column2='invoice_id',
    #     string='Invoices'
    # )
    # invoice_60_90 = fields.Many2many(
    #     comodel_name='account.invoice',
    #     relation='wizard_ar_ap_invoice_60_90_rel',
    #     column1='wizard_id',
    #     column2='invoice_id',
    #     string='Invoices'
    # )
    # invoice_90_120 = fields.Many2many(
    #     comodel_name='account.invoice',
    #     relation='wizard_ar_ap_invoice_90_120_rel',
    #     column1='wizard_id',
    #     column2='invoice_id',
    #     string='Invoices'
    # )
    # invoice_120_ = fields.Many2many(
    #     comodel_name='account.invoice',
    #     relation='wizard_ar_ap_invoice_120_rel',
    #     column1='wizard_id',
    #     column2='invoice_id',
    #     string='Invoices'
    # )

    report_type = fields.Selection(
        [("detail", "Detail"), ("summary", "Summary")], string='Type', default="detail")

    def get_digits(self, name):
        digit = self.env['decimal.precision'].search(
            [('name', '=', name)], limit=1)
        return digit.digits
    
    def get_0_to_30(self, partner_id):
        # get 0 to 30
        date_0_to_30 = (datetime.strptime(self.period_date,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        # date_0_to_30 = self.period_date - relativedelta(days=30)
        invs = self.invoice_ids.filtered(lambda x : x.date_due >= date_0_to_30 and x.date_due <= self.period_date and x.partner_id.id == partner_id )
        # self.invoice_0_30 = invs
        return invs
    
    def get_30_to_60(self, partner_id):
        # get 0 to 30
        date_0_to_30 = (datetime.strptime(self.period_date,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_30_to_60 = (datetime.strptime(date_0_to_30,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        # date_0_to_30 = self.period_date - relativedelta(days=30)
        invs = self.invoice_ids.filtered(lambda x : x.date_due >= date_30_to_60 and x.date_due < date_0_to_30 and x.partner_id.id == partner_id )
        # self.invoice_0_30 = invs
        return invs
    
    def get_60_to_90(self, partner_id):
        # get 0 to 30
        date_0_to_30 = (datetime.strptime(self.period_date,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_30_to_60 = (datetime.strptime(date_0_to_30,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_60_to_90 = (datetime.strptime(date_30_to_60,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        # date_0_to_30 = self.period_date - relativedelta(days=30)
        invs = self.invoice_ids.filtered(lambda x : x.date_due >= date_60_to_90 and x.date_due < date_30_to_60 and x.partner_id.id == partner_id )
        # self.invoice_0_30 = invs
        return invs
    
    def get_90_to_120(self, partner_id):
        # get 0 to 30
        date_0_to_30 = (datetime.strptime(self.period_date,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_30_to_60 = (datetime.strptime(date_0_to_30,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_60_to_90 = (datetime.strptime(date_30_to_60,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_90_to_120 = (datetime.strptime(date_60_to_90,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        # date_0_to_30 = self.period_date - relativedelta(days=30)
        invs = self.invoice_ids.filtered(lambda x : x.date_due >= date_90_to_120 and x.date_due < date_60_to_90 and x.partner_id.id == partner_id )
        # self.invoice_0_30 = invs
        return invs
    
    def get_120_more(self, partner_id):
        # get 0 to 30
        date_0_to_30 = (datetime.strptime(self.period_date,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_30_to_60 = (datetime.strptime(date_0_to_30,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_60_to_90 = (datetime.strptime(date_30_to_60,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_90_to_120 = (datetime.strptime(date_60_to_90,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        date_120_to_more = (datetime.strptime(date_90_to_120,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        # date_0_to_30 = self.period_date - relativedelta(days=30)
        invs = self.invoice_ids.filtered(lambda x : x.date_due < date_90_to_120 and x.partner_id.id == partner_id )
        # self.invoice_0_30 = invs
        return invs

    def process_wizard(self):
        invoices = self.env['account.invoice'].search(
            [('state', '=', 'open'), ("date_invoice", "<=", self.period_date)])

        if self.account_type == 'ar':
            invoices = self.env['account.invoice'].search(
                ['&', '&', ('state', '=', 'open'), ('type', '=', 'out_invoice'), ("date_invoice", "<=", self.period_date)])
        elif self.account_type == 'ap':
            invoices = self.env['account.invoice'].search(
                ['&', '&', ('state', '=', 'open'), ('type', '=', 'in_invoice'), ("date_invoice", "<=", self.period_date)])

        self.invoice_ids = invoices

        # # get 0 to 30
        # date_0_to_30 = (datetime.strptime(self.period_date,'%Y-%m-%d') - relativedelta(days=30)).strftime('%Y-%m-%d')
        # # date_0_to_30 = self.period_date - relativedelta(days=30)
        # invs = self.invoice_ids.filtered(lambda x : x.date_due >= date_0_to_30 and x.date_due <= self.period_date )
        # self.invoice_0_30 = invs

        # mapping partners
        self.partner_ids = invoices.mapped('partner_id')

        # testing code
        # print("------------------------------------------------")
        # print("Testing Invoice Filtering")
        # invs = self.invoice_ids.filtered(lambda x : (x.date_due - self.period_date).days > 0 )
        # pprint(invs)
        # print("------------------------------------------------")

        action = self.env.ref('gekha_mod.gekha_ar_ap_report_action').read()[0]
        return action

        # call by report id
        # return self.env['report'].get_action(self, 'gekha_mod.gekha_ar_ap_report_template', date={'orientation': 'Landscape'})

        # call by action
        # return self.env.ref('gekha_mod.gekha_ar_ap_report_action')

        # return {
        #     'type': 'ir.actions.report.xml',
        #     'name': 'Sales Report',
        #     'res_model': 'wizard.ar.ap',
        #     'res_id': self.id,
        #     'report_type': 'qweb-pdf',
        #     'paperformat': 'gekha_mod.gekha_report_a4_landscape',
        #     'report_name': 'gekha_mod.gekha_ar_ap_report_template',
        # }

        # return self.env['report'].with_context(landscape=True).get_action(self, 'gekha_mod.gekha_ar_ap_report_template')
