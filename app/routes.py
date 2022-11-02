from crypt import methods
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet_model import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        color=request_body["color"],
        size=request_body["size"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planet_response = []

    name_query = request.args.get("name")
    color_query = request.args.get("color")
    queries_hash = {"name": name_query,
                    "color": color_query}

    for query_key, query_var in queries_hash.items():
        print(query_key)
        if query_var:
            planets = Planet.query.filter_by(query_key=query_var)
        else:
            planets = Planet.query.all()

    planets = Planet.query.all()

    # planet_response = [vars(planet) for planet in planets]

    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        })

    return jsonify(planet_response)


def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_planet(planet_id):
    planet = validate_planet_id(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size
    }


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet_id(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

# @planets_bp.route("/<planet_id>", methods=["PATCH"])
# def edit_planet(planet_id):
