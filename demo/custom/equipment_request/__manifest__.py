{
    'name': "equipment request",
    'version': '1.0',
    'depends': ['base',],
    'author': "Author Name",
    'license': 'LGPL-3',
    'category': 'Category',
    'description': """
    Description text 
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'view/request_view.xml',
        'view/request_menus.xml'
        ],
    # data files containing optionally loaded demonstration data
    'demo': [],
}