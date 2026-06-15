from odoo import fields ,fields 

class MrpProduction (models.Model):
  inherit ="mrp.production"
  
  #relations
  production_line=fields.One2many(
  "production.line",
  string="Production Line"
)
  machine =fields.One2many (
  "machine", 
  string ="Machine"
)
  shift =fields.One2many (
 "shift",
string ="Shift"
)

  #fields 
  production_code=fields.Char (
    copy =False, 
    readonly =True,
    string ="Production code"
)

start =fields.Float(
string ="Start"
)

end =fields.Float(
string ="End"
)

good=fields.Float (
string ="Good"
)

scrap=fields.Float (
 string ="Scrap"
)