from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charges = fields.Float(string='Delivery Charges', invisible=True)

    def _prepare_invoice(self):
        """
        Override to include delivery charges in the invoice.
        """
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        # Add delivery charges to invoice
        invoice_vals.update({
            'delivery_charges': self.delivery_charges,
        })
        return invoice_vals


class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_charges = fields.Float(string='Delivery Charges', invisible=True)

    @api.model
    def create(self, vals):
        """
        When an invoice is created, automatically add the delivery charges as an invisible field
        but don't show it in the invoice lines.
        """
        invoice = super(AccountMove, self).create(vals)

        # If delivery charges exist, add them to the invoice
        if invoice.move_type == 'out_invoice' and invoice.delivery_charges:
            # Create an invoice line for delivery charges
            invoice_line_vals = {
                'move_id': invoice.id,
                'name': 'Delivery Charges',
                'quantity': 1,
                'price_unit': invoice.delivery_charges,
                'account_id': self.env['ir.property'].get('property_account_income_categ_id').id,
                'display_type': 'line_section',  # This ensures it doesn't appear in the invoice lines
            }
            self.env['account.move.line'].create(invoice_line_vals)

        return invoice
