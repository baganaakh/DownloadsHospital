{
    'name': 'RFID integration to ERP',
    'version': '0.1',
    'category': 'Extra Tools',
    'summary': 'Таг бүртгэл',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Алтанбагана',
    'maintainer': 'baganaakh@gmail.com',
    'website': 'http://baganaakh.blogspot.com',
    'live_test_url': '',
    'depends': ['mail','sale'],
    'demo': [],
    'data': [
        'views/patient.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv'
    ],
    'images': ['static/description/rfidIcon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# Video Explanation: https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1
