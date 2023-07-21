from odoo import http

class Motor(http.Controller):
    @http.route('/kwaiil/')
    def index(self, **kw):
        return 'Hello World'
    
    @http.route('/kwaiil/motos/', auth='public', website=True)
    def motos(self, **kw):
        # motos = http.request.env['product.template'].search([])
        motos = http.request.env['product.template'].search([('detailed_type', '=' , 'motorcycle')])
        return http.request.render('motor-registry.motor_website',{
            'motos':motos,
        })