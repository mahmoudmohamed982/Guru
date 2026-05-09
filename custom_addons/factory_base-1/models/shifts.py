from odoo import models, fields, api

class FactoryShift(models.Model):
    _name = "factory.shift"
    _description = "Factory Shift"

    name = fields.Char(string="Shift Name", required=True)
    code = fields.Char(string="Reference", copy=False, readonly=True)

    active = fields.Boolean(default=True)

    start_time = fields.Float(string="Start Time")
    end_time = fields.Float(string="End Time")

    notes = fields.Text(string="Notes")

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('factory.shift')
        return super().create(vals)