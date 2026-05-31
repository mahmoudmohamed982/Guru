from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit="sale.order.line"
    thickness = fields.Float(string="Thickness (mm)")
    length = fields.Float(string="Length (mm)")
    color = fields.Selection([
    ('white','White'),
    ('black','Black'),
    ('blue','Blue'),
    ('gray','Gray')]
    ,string="Color")
    material_grade = fields.Char(string="Material Grade")
    priority = fields.Selection([('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent'),],default='normal', string="Mfg Priority")