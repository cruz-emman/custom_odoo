{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Managment System',
    'description': """Hospital Manegment""",
    'depends': ['mail.thread', 'mail.activity.mixin'],
    'data': [
         'security/ir.model.access.csv',
         'views/menu.xml',
         'views/patient.xml',
         'views/female_patient_view.xml'
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_installable': False,
    'assets': {},
    'license': 'LGPL-3'

}