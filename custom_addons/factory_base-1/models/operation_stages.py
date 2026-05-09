from odoo import models, fields, api

class OperationStage(models.Model):
    _name = "factory.operation.stage"
    _description = "Operation Stage"

    name = fields.Char(string="Operation Stage Name", required=True)
    code = fields.Char(string="Reference", copy=False, readonly=True)
    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('factory.operation.stage')
        return super().create(vals)