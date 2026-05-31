{
    'name': 'Factory Sales & Planning',
    'author': 'SW:Mahmoud',
    'version': '17.0.1.0.0',
    'summary': 'Sales technical specs and production planning requests',
    'category': 'Manufacturing',
    'depends': ['base', 'sale', 'factory_base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/production_request.xml',
        'views/sale_order.xml',
    ],
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
}