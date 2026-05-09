from odoo import models, fields, api

class ProductionLines(models.Model):
    _name = "factory.production.line"
    _description = "Production Lines"

    name = fields.Char(string="Line Name", required=True)
    code = fields.Char(string="Reference", copy=False, readonly=True)
    active = fields.Boolean(default=True)

    machine_ids = fields.One2many(
        'factory.machine',
        'production_line_id',
        string="Machines"
    )

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('factory.production.line')
        return super().create(vals)