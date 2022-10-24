from crypt import methods
from flask import Blueprint, jsonify, abort, make_response


class Planet:

    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size


planets = [
    Planet(1, "Mercury", "Description Mercury", "Mercury size"),
    Planet(2, "Venus", "Description Venus", "Venus size"),
    Planet(3, "Earth", "Description Earth", "Earth size"),
    Planet(4, "Mars", "Description Mars", "Mars size"),
    Planet(5, "Jupiter", "Description Jupiter", "Jupiter size"),
    Planet(6, "Saturn", "Description Saturn", "Saturn size"),
    Planet(7, "Uranus", "Description Uranus", "Uranus size"),
    Planet(8, "Neptune", "Description Neptune", "Neptune size")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planet_response = []
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

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = validate_planet_id(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size
    }
