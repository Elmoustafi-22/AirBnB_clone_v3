#!/usr/bin/python3
"""All default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from flask import abort, request, jsonify


@app_views.route("/cities/<city_id>/places", strict_slashes=False,
                 methods=["GET"])
def places(city_id):
    """show places"""
    places_list = []
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = city.places
    for place in places:
        places_list.append(place.to_dict())
    return jsonify(places_list)


@app_views.route("/places/<place_id>", strict_slashes=False, methods=["GET"])
def get_place(place_id):
    """Gets a City object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>", strict_slashes=False,
                 methods=["DELETE"])
def place_delete(place_id):
    """delete place method"""
    obj = storage.get(Place, place_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
