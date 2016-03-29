# -*- coding: utf-8 -*-
from openerp import http

# class IaPdfreportTemplate(http.Controller):
#     @http.route('/ia_pdfreport_template/ia_pdfreport_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ia_pdfreport_template/ia_pdfreport_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ia_pdfreport_template.listing', {
#             'root': '/ia_pdfreport_template/ia_pdfreport_template',
#             'objects': http.request.env['ia_pdfreport_template.ia_pdfreport_template'].search([]),
#         })

#     @http.route('/ia_pdfreport_template/ia_pdfreport_template/objects/<model("ia_pdfreport_template.ia_pdfreport_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ia_pdfreport_template.object', {
#             'object': obj
#         })