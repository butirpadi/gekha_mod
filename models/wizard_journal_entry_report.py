from odoo import fields, models, api, _
from odoo.exceptions import UserError


class JournalEntryReportWizard(models.TransientModel):
    _name = 'journal.entry.report.wizard'

    name = fields.Char(string='Name', default="New")
    date_from = fields.Date(string='Start Date')
    date_to = fields.Date(string='End Date')
    journal_ids = fields.Many2many(
        comodel_name='account.journal',
        relation='wizard_journal_entries_report_journal_rel',
        column1='wizard_id',
        column2='journal_id',
        string='Journals'
    )
    account_move_ids = fields.Many2many(
        comodel_name='account.move',
        relation='wizard_journal_entries_report_account_move_rel',
        column1='wizard_id',
        column2='move_id',
        string='Journal Entry'
    )

    def process_wizard(self):
        if self.journal_ids:
            move_ids = self.env['account.move'].search(
                ['&', '&', ('date', '>=', self.date_from), ('date', '<=', self.date_to), ('journal_id', 'in', self.journal_ids.ids)])
        else:
            move_ids = self.env['account.move'].search(
                [('date', '>=', self.date_from), ('date', '<=', self.date_to)])

        self.update({
            'account_move_ids': move_ids
        })

        return self.env['report'].get_action(self, 'gekha_mod.gekha_journal_entry_report_template')

    def get_digits(self, name):
        digit = self.env['decimal.precision'].search(
            [('name', '=', name)], limit=1)
        return digit.digits
