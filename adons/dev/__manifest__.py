# -*- coding: utf-8 -*-

{
    'name': 'Development module-name'
    , 'version': '13.0.0.1'
    , 'summary': 'Dev module-name summary'
    , 'description': """"
        Development module-name
        ====================
        Development module-name http://www.alldomain.biz/docs/odoo/13/dev/modulename
    """
    , 'author': 'All Domain Soluiton LLC'
    , 'website': 'http://www.alldomain.biz'
    , 'support': 'admin@alldomain.biz'
    , 'license': 'LGPL-3'

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    , 'category': 'Uncategorized'
    
    , 'images': [
		'static/description/icon.png'
	]

    # any module necessary for this one to work correctly
    , 'depends': [
        'base'
        # , 'product'
        # , 'stock'
	]
    
    # always loaded
    , 'data': [
        # 'security/ir.model.access.csv'
        'views/views.xml'
        , 'views/templates.xml'
        # , 'wizard/dev_module.xml'
    ]
    # only loaded in demon stration mode
    , 'demo': [
        # 'demo/demo.xml'
        # , 'demo/dev_demo.xml'
    ]
    
    # , 'test': [
        # 'test/test.xml'
    # ]
    # , 'qweb': [
        # 'qweb/qweb.xml'
    # ]
    # , 'css': [
        # 'css/css.xml'
    # ]
    , 'application'   : True
    , 'installable'   : True
    , 'auto_install'  : False
}
