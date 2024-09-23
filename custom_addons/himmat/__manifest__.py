{
    'name': 'Himmat',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Group and Participant management',
    'description': 'Module to manage groups and participants.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/group_views.xml',
        'views/participant_views.xml',
    ],
    'installable': True,
    'application': True,
}
