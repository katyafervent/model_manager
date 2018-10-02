import logging

from flask import request
from flask_restplus import Resource
from api.directory.serializers import user
from api.restplus import api
from database.models import Organization

log = logging.getLogger(__name__)

ns = api.namespace('directory/organizations', description='Organization related operations')

