{
    'name': 'Dokumentų Valdymo Modulis',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Saugoti informacijai apie įvairius dokumentus ar knygas.',
    'description': """
        Šis modulis skirtas saugoti informacijai apie įvairius dokumentus ar knygas.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/document_views.xml',
        'views/actions.xml',
        'views/wizard_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
