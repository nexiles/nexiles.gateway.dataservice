# -*- coding: utf-8 -*-
#
# File: production.py
#
# Copyright (c) nexiles GmbH
__author__    = """Stefan Eletzhofer <se@nexiles.de>"""
__docformat__ = 'plaintext'
__revision__  = "$Revision: $"
__version__   = '$Revision: $'[11:-2]

import flask
import logging
import mimetypes

from nexiles.tools import json
from nexiles.tools import utils
from nexiles.tools import query
from nexiles.tools import content

from nexiles.tools.rest import APIError
from nexiles.tools.rest import handle_api_error
from nexiles.tools.rest import returns_json
from nexiles.tools.rest import inject_runtime

__all__ = ["blueprint"]

logger = logging.getLogger("nexiles.gateway.dataservice")

blueprint = flask.Blueprint("dataservice", __name__)


def get_by_number(number):
    """get_by_number(number) -> obj
    """
    res = query.find("wt.doc.WTDocument", number=number)
    if res:
        return res[0][1]


def get_json_data(doc, name):
    """get_json_data(doc, name) -> JSON
    """
    mimetype, _ = mimetypes.guess_type(name)
    if mimetype != "application/json":
        raise APIError(400, "illegal request", "can only serve JSON")

    filepath = content.get_content_file(doc, name)
    if not filepath:
        raise APIError(404, "not found", "%s" % name)

    return json.loads(file(filepath).read())


def query_data(data, id, **kw):
    # XXX: 'items' need to come from the data itself
    for item in data["items"]:
        if str(item["id"]) == str(id):
            return item


@blueprint.route("/<number>/<name>", methods=["GET"])
@handle_api_error
@returns_json
@inject_runtime
def get(number, name):
    """get(number, name) -> JSON

    Data service

    :params number:  the number of a content holder
    :params name:    the name of a content item

    :returns: JSON data
    """
    logger.debug("DataService.get(%s %s)" % (number, name))

    if not number:
        raise APIError(400, "illegal request", "need number.")

    doc = get_by_number(number)
    if not doc:
        raise APIError(404, "not found", "%s" % number)

    if not name:
        raise APIError(400, "illegal request", "need name.")

    data = get_json_data(doc, name)
    return data

@blueprint.route("/<number>/<name>/<id>", methods=["GET"])
@handle_api_error
@returns_json
@inject_runtime
def get_id(number, name, id):
    """get(number, name, id) -> JSON

    Data service

    :params number:  the number of a content holder
    :params name:    the name of a content item
    :params id:      the id of an item

    :returns: JSON data
    """
    logger.debug("DataService.get_id(%s %s %s)" % (number, name, id))

    if not number:
        raise APIError(400, "illegal request", "need number.")

    doc = get_by_number(number)
    if not doc:
        raise APIError(404, "not found", "%s" % number)

    if not name:
        raise APIError(400, "illegal request", "need name.")

    if not id:
        raise APIError(400, "illegal request", "need id.")

    data = get_json_data(doc, name)

    item = query_data(data, id)
    if item:
        return item

    raise APIError(404, "not found", "%s/%s" % (name, id))


@blueprint.route("/<number>/<name>/<id>", methods=["POST"])
@handle_api_error
@returns_json
@inject_runtime
def post(number, name, id=None):
    logger.debug("DataService.post(%s %s %s)" % (number, name, id))
    return {}


@blueprint.route("/<number>/<name>/<id>", methods=["DELETE"])
@inject_runtime
@returns_json
@handle_api_error
def delete(number, name, id=None):
    logger.debug("DataService.delete(%s %s %s)" % (number, name, id))
    return {}


# vim: set ft=python ts=4 sw=4 expandtab :
