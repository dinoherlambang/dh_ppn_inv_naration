{
    'name': 'Custom Invoice Report PPN',
    'version': '13.0.1.0.0',
    'summary': 'Add PPN narration text to invoice reports',
    'description': '''
        This module adds standardized PPN narration text to invoice reports
        based on PMK 131/2024 regulations.
        Features:
        - Adds automatic PPN 11% narration
        - Implements PMK compliance text
    ''',
    'category': 'Accounting',
    'author': 'Dino Herlambang',
    'website': 'https://github.com/dinoherlambang',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/report_invoice_document_inherit.xml',
    ],
    'images': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
