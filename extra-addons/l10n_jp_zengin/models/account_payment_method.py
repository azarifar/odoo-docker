# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        res['zengin'] = {
            'mode': 'multi',
            'domain': [('type', '=', 'bank')],
            'currency_ids': self.env.ref("base.JPY").ids,
        }
        return res
