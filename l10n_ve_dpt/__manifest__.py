#    Copyright (C) 2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2019 Konos CL (<http://www.konos.cl/>).

{
    "name": "Municipios y Parroquias de Venezuela",
    "summary": "Polular Base de datos de Municipios y Parroquias de Venezuela",
    "description": """
Localización Venezolana: Municipios y Parroquias
================================================

Basado en BachacoVE e información del INE del año 2013, añade los campos de municipio y parroquia en el modelo `res.partner` de
manera que queden disponibles en todos los campos de dirección en modelos derivados como `res.users` o `res.company`.
     """,
    "author": "LerCLoud, " "Konos, " "BachacoVE",
    "website": "https://lercloud.com",
    "category": "Venezuela Localization",
    "version": "13.0.3.0.0",
    "depends": ["base"],
    "data": [
        "data/res.country.state.xml",
        "data/res.country.state.municipality.xml",
        "data/res.country.state.municipality.parish.xml",
        "views/l10n_ve_dpt_view.xml",
        "views/res_partner.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "installable": True,
}
