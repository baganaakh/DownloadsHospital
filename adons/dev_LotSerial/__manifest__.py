# -*- coding: utf-8 -*-
{
    'name': 'Development star'

    , 'description': """
        Long description of module's purpose
    """

    , 'author': 'Алтанбагана'
    , 'website': 'http://baganaakh.blogspot.com'

    , 'maintainer': 'baganaakh@gmail.com'

    , 'version': '13.0.0.0.1'
    , 'category': 'Extra Tools'
    , 'summary': 'Анхан шатны Odoo Хөгжүүлэлт'
    , 'sequence': '10'
    , 'license': 'AGPL-3'

    # any module necessary for this one to work correctly
    , 'depends': ['base']

    # always loaded
    , 'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
        , 'views/templates.xml'
    ]
    # only loaded in demonstration mode
    , 'demo': [
        'demo/demo.xml'
    ]
}
