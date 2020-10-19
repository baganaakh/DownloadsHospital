# -*- coding: utf-8 -*-

from odoo import http

import logging

_logger = logging.getLogger(__name__)

class Dev(http.Controller):
    @http.route(
        '/dev/modulename/'
        , auth='public'
        # , auth = 'none'
        # , auth = "user"
        # , type = 'http'
        # , type = 'json'
        # , methods = ['POST']
        # , methods = ['GET']
        # , website = True
        # , csrf = False
    )
    def index(self, **kw):
        _logger.critical('!!! 23 str( self )  = "' + str( self ) + '" !!!')
        return "Development module-name"

    @http.route(
        '/dev/modulename/objects/'
        , auth='public'
        # , auth = 'none'
        # , auth = "user"
        # , type = 'http'
        # , type = 'json'
        # , methods = ['POST']
        # , methods = ['GET']
        # , website = True
        # , csrf = False
    )
    def list(self, **kw):
        _logger.critical('!!! 39 str( self )  = "' + str( self ) + '" !!!')
        return http.request.render('dev_modulename.listing', {
            'root': '/dev/modulename',
            'objects': http.request.env['dev.modelname'].search([]),
        })

    @http.route(
        '/dev/modulename/objects/<model("dev.modelname"):obj>/'
        , auth='public'
        # , auth = 'none'
        # , auth = "user"
        # , type = 'http'
        # , type = 'json'
        # , methods = ['POST']
        # , methods = ['GET']
        # , website = True
        # , csrf = False
    )
    def object(self, obj, **kw):
        _logger.critical('!!! 58 str( self )  = "' + str( self ) + '" !!!')
        return http.request.render('dev_modulename.object', {
            'object': obj
        })
    
