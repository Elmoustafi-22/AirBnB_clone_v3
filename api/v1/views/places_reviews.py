#!/usr/bin/python3

from api.v1.views import app_views
from models import storage
from models.place import Place
from models.user import User
from models.review import Review
from flask import abort, request, jsonify


@app_views.route("/places/<place_id>/reviews", methods=["GET"])
def review(place_id):
    reviews_list = []
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = place.reviews
    for review in reviews:
        reviews_list.append(review.to_dict())
    return jsonify(review_list)



@app_views.route("/reviews/<review_id>", methods=["GET"])
def get_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    obj = storage.get(Review, review_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/reviews", methods=["POST"])
def create_review(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    if "user_id" not in data:
        abort(400, "Missing user_id")
    user = storage.get(User, data["user_id"])
    if user is None:
        abort(404)
    if "text" not in data:
        abort(400, "Missing text")
    new_review = Review(place_id=place.id, **data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201



@app_views.route("/reviews/<review_id>", methods=["PUT"])
def update_review(review_id):
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    review.text = data.get("text", review.text)
    review.save()
    return jsonify(review.to_dict())
