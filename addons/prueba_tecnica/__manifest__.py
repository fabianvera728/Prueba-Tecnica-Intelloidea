{
    "name": "Prueba tecnica",
    "author": "Fabian Vera",
    "version": "1.0",
    "summary": "Prueba tecnica",
    "sequence": 10,
    "description": """Prueba tecnica""",
    "category": "Productivity",
    "depends": ['base', 'sale', 'product', 'project'],
    "data": [
        "security/ir.model.access.csv",
        "views/contact.xml",
        "views/product.xml",
        "views/user.xml",
        "views/quotation.xml",
        "views/activities.xml"
    ],
    "demo": [],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": True
}