import pytest
from app import create_app
from app import db
from flask.signals import request_finished
# from app.models.planet_model import Planet


def test_get_no_planets(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_not_found(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 1 not found"}


def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Mercury",
            "description": "First planet in the solar system",
            "color": "blue",
            "size": 1617,
            "satellite": False
        },
        {
            "id": 2,
            "name": "Venus",
            "description": "Second planet in the solar system",
            "color": "yellow",
            "size": 7520,
            "satellite": False
        }
    ]


def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "Third planet in the solar system",
        "color": "blue",
        "size": 2620,
        "satellite": True
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"
