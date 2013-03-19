# -*- coding: utf-8 -*-
#
# Copyright (c) nexiles GmbH
#
"""nexiles|gateway data service"""

__author__    = """Stefan Eletzhofer <se@nexiles.de>"""

import os
import sys
import logging

import flask

from nexiles.tools.rest.services import service_base_url

from nexiles.gateway.dataservice import version
from nexiles.gateway.dataservice import dataservice

__version__ = version.__version__
__build__   = version.__build__
__date__    = version.__date__

logger = logging.getLogger("nexiles.gateway.dataservice")


def register(app):
    """register(app) -> new app

    Register the data service.

    :returns: flask app
    """
    logger.info("register: app=%r" % app)

    app.register_blueprint(dataservice.blueprint,
            url_prefix=service_base_url+"/dataservice")

    return app

# vim: set ft=python ts=4 sw=4 expandtab :

