from odoo import models, fields, api

class ScrapReason(models.Model):
    _name = "factory.scrap.reason"
    _description = "Scrap Reason"

    name = fields.Char(string="Scrap Reason Name", required=True)
    code = fields.Char(string="Reference", copy=False, readonly=True)
    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('factory.scrap.reason')
        return super().create(vals)