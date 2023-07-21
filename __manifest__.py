{
    'name': 'Motorcycle Registry',
    'summary' : 'Manage Registration of Motorcycles',
    'description' : """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
    """,
    'license' : 'OPL-1',
    'author' : 'Mauricio Rubio',
    'website' : 'www.odoo.com',
    'category' : 'Custom Modules / Technical Training',
    'depends' : ['sale','stock', 'website'],
    'data': [
        'security/kwaiil_groups.xml',
        'security/ir.model.access.csv',
        'data/registry_data.xml',
        'views/kwaii_menu_items.xml',
        'views/kwaiil_registry_views.xml',
        'views/motorcycle_view.xml',
        'views/motorcycle_templates.xml'

    ],
    'demo': [
        'demo/motor_registry_demo.xml'
    ],
    'application' : True,
}   