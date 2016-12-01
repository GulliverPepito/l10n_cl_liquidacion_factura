# -*- coding: utf-8 -*-
from openerp import http

# class L10nClLiquidacionFactura(http.Controller):
#     @http.route('/l10n_cl_liquidacion_factura/l10n_cl_liquidacion_factura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_liquidacion_factura/l10n_cl_liquidacion_factura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_liquidacion_factura.listing', {
#             'root': '/l10n_cl_liquidacion_factura/l10n_cl_liquidacion_factura',
#             'objects': http.request.env['l10n_cl_liquidacion_factura.l10n_cl_liquidacion_factura'].search([]),
#         })

#     @http.route('/l10n_cl_liquidacion_factura/l10n_cl_liquidacion_factura/objects/<model("l10n_cl_liquidacion_factura.l10n_cl_liquidacion_factura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_liquidacion_factura.object', {
#             'object': obj
#         })