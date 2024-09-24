# -*- coding: utf-8 -*-
# from odoo import http


# class TaskModule(http.Controller):
#     @http.route('/task_module/task_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_module/task_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_module.listing', {
#             'root': '/task_module/task_module',
#             'objects': http.request.env['task_module.task_module'].search([]),
#         })

#     @http.route('/task_module/task_module/objects/<model("task_module.task_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_module.object', {
#             'object': obj
#         })

