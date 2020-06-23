#    Copyright (C) 2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2019 Konos CL (<http://www.konos.cl/>).
{
    "name": "Municipios y Parroquias de Venezuela",
    "summary": "Polular Base de datos de Municipios y Parroquias de Venezuela",
    "author": "LerCLoud, " "Konos, " "BachacoVE",
    "website": "https://lercloud.com",
    "category": "Venezuela Localization",
    "version": "13.0.3.0.0",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        "data/res.country.state.xml",
        "data/res.country.state.municipality.xml",
        "data/res.country.state.municipality.parish.xml",
        "views/l10n_ve_dpt_view.xml",
        "views/res_partner.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
