{
    'name':'Factory Base',
    'author':'SW:Mahmoud',
    'version':'17.0.1.0.0',
    'description':'type later',
    'summary':'Core management for factory operations and production lines',
    'category':'Manufacturing',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/production_lines.xml',
        'views/machines.xml',
        'views/operation_stages.xml',
        'views/scrap_reasons.xml',
        'views/shifts.xml',
        'views/downtime_reasons.xml'
    ],
    'license':'LGPL-3',
    'application':True,
    'installable':True

}