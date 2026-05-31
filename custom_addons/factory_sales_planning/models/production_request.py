from odoo import models,fields, api 

class ProductionRequest(Models.model):
    _name="production.request"
    _description="Production Request"

    # =========================
    # relations
    # =========================

    sale_order_id=fields.Many2one(
        "sale.order",
        string="order id"
    )

    production_request_lines=fields.One2many(
        "production.request.lines",
        "production_request_id",
        string="production request lines"
    )



    # =========================
    # fields
    # =========================

    name=fields.Char(
        string="pr/ref",
        readonly=True,
        copy=False
    )

    