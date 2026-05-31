from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit='sale.order'

    production_request_ids=fields.One2many(
        'factory.production.request',
        'sale_order_id',
        string='Productiom Requests'
    )

    production_request_count=fields.Integer( 
        compute='_compute_production_reqest_count',
        store=True,
        readonly=True
    )


    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            order._create_production_request()
        return res
    @api.depends('production_request_ids')
    def _compute_production_reqest_count(self):
        for rec in self:
            rec.production_request_count=len(rec.production_request_ids)

    def _create_production_request(self):
        lines = []

        for line in self.order_line:
            lines.append((0,0,{ 
                "thikness": "line.thikness", 
                "color":"line.color"
            }))
        self.env['factory.production.request'].create(

            {
                "sale_order_id":self.id, 
                "lines_ids":lines
            }
        )
    
    def _view_production_request(self):
        return{
            "type":"ir.actions.act_window",
            "name":"Production Requests",
            "res_model":"factory.production.request", 
            "view_mode":"tree,form", 
            "domain":[("sale_order_id","=",self.id)],
            "context":{"default_sale_order_id":self.id}
        }