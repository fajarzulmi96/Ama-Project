from odoo import api, _, fields, models

class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    ama_onhand_quantity = fields.Float(string="On Hand Total", compute="_compute_onhand", digits=(16,3))
    ama_reserve_quantity = fields.Float(string="Reserved Total", compute="_compute_reserve", digits=(16,3))

    @api.depends('location_id', 'product_id')
    def _compute_onhand(self):
        for rec in self :
            stock_location = rec.location_id
            product = rec.product_id
            var = rec.product_stock_quant_ids.filtered(lambda e:e.location_id.id == stock_location.id and e.product_id.id == product.id).mapped('quantity')
            rec.ama_onhand_quantity = sum(var)
    
    @api.depends('location_id', 'product_id')
    def _compute_reserve(self):
        for rec in self :
            stock_location = rec.location_id
            product = rec.product_id
            var = rec.product_stock_quant_ids.filtered(lambda e:e.location_id.id == stock_location.id and e.product_id.id == product.id).mapped('reserved_quantity')
            rec.ama_reserve_quantity = sum(var)