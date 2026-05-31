from odoo import models,fields, api 
from odoo.exceptions import UserError

class FactoryProductionRequest(models.Model):
    _name="factory.production.request", 
    _description="Factory Production Request",
    _inherit=["mail.thread",",mail.activity.mixin"]
    _order="id desc", 

    #Relations
    sale_order_id=fields.Many2one("sale.order",string="Sale order")

    line_ids=fields.One2many(
        "factory_production_request_line", 
        "factory.production.request", 
    )

    #fields

    partner_id=fields.Char( 
        related=sale_order_id.partner_id.id,
        store=True,

    )

    name=fields.Char(
        copy=False,
        readonly=True,
        string="Request Reference",
        default="New"
    )

    state=fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
        ],traking=True, string="State" , default='draft')

    date_request-fields.Date(
        string="Request Date",
        default=fields.Date.today
    )
    date_planned=fields.Date( 
        string="Planned Date",
    )
    note=fields.Text(string="Note")

    #methods
    @api.model
    def create(self,vals):
        res=super().create(vals)
        for req in self:
            if vals.get("name","New")=="New":
                vals["name"]=self.env['ir.sequence'].next_by_code('factory.production.request')
            return res
    def action_confirm(self):
        for rec in self:   
           if rec.state !="draft":
             raise UserError("Only draft requests can be confirmed")
        rec.state='confirm'

    def action_in_progress(self):
        for rec in self:   
           if rec.state !="confirmed":
             raise UserError("Only confirmed requests can be in progres")
        rec.state='in_progress'

    def action_done(self):
        for rec in self:
            if rec.state != 'in_progress':
                raise UserError("Only in-progress requests can be marked as done.")
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            if rec.state == 'done':
                raise UserError("Cannot cancel a done request.")
            rec.state = 'cancelled'

    def action_reset_draft(self):
        for rec in self:
            if rec.state != 'cancelled':
                raise UserError("Only cancelled requests can be reset to draft.")
            rec.state = 'draft'
    

class FactoryProductionRequestLine(models.Model):
    _name="factory.production.request.line", 
    _description="Factory Production Request Line",

    #Relations
    request_id=fields.Many2one(
        "factory.production.request",
        string="Production Request",
        ondelete='casecade'
    )

    sale_line_id=fields.Many2one(
        'sale.order.line'
    )

    #fields
    product_id=fields.Char(
        related=sale_line_id.product_id.id
    ) 

    qty_planned=fields.Float(string="Planned Qty", required=True)
    uom_id = fields.Many2one(
        related='sale_line_id.product_uom',
        string="Unit of Measure",
        store=True
    )
        
    thickness = fields.Float(string="Thickness (mm)")
    length = fields.Float(string="Length (mm)")
    color = fields.Char(string="Color")
    material_grade = fields.Char(string="Material Grade")
    priority = fields.Selection([
        ('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], default='normal', string="Priority")
    note = fields.Text(string="Notes")