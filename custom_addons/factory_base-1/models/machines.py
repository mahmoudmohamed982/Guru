from odoo import models, fields, api

class Machines(models.Model):
    _name = "factory.machine"
    _description = "Machines"

    name = fields.Char(string="Machine Name", required=True)
    code = fields.Char(string="Reference", copy=False, readonly=True)
    production_line_id = fields.Many2one('factory.production.line', string="Production Line")
    active = fields.Boolean(default=True)
    serial_number = fields.Char(string="Serial Number")
    manufacturer = fields.Char(string="Manufacturer")
    notes = fields.Text(string="Notes")

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('factory.machine')
        return super().create(vals)