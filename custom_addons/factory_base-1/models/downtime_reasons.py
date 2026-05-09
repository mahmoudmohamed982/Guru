from odoo import models, fields, api

class DowntimeReason(models.Model):
    _name = "factory.downtime.reason"
    _description = "Downtime Reasons"

    name = fields.Char(string="Downtime Reason Name", required=True)
    code = fields.Char(string="Reference", copy=False, readonly=True)

    category = fields.Selection([
        ('machine', 'Machine'),
        ('material', 'Material'),
        ('operator', 'Operator'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other')
    ], string="Category")

    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('factory.downtime.reason')
        return super().create(vals)