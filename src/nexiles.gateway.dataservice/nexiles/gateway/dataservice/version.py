# -*- coding: utf-8 -*-
#
# File: version.py
#
# Copyright (c) nexiles GmbH
__author__    = """Stefan Eletzhofer <se@nexiles.de>"""
__docformat__ = 'plaintext'
__revision__  = "$Revision: $"
__version__   = '$Revision: $'[11:-2]


__version__ = "0.1dev"
__build__   = 10
__date__    = "2013-03-19"

from nexiles.tools.rest import returns_json
from dataservice import blueprint

@blueprint.route("/version", methods=["GET"])
@returns_json
def version():
    return {
        "version": __version__,
        "build": __build__,
        "date": __date__
    }


# vim: set ft=python ts=4 sw=4 expandtab :
