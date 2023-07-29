from flask import Blueprint
from flask_restful import Api
from views.moves import Moves


# Create the Blueprint
api_blueprint = Blueprint('api', __name__)

# Create the API and add the resources to it
urls = Api(api_blueprint)

urls.add_resource(Moves, '/chess/<string:slug>')