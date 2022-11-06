import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet_model import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    planet_1 = Planet(
        name="Mercury",
        description="First planet in the solar system",
        color="blue",
        size=1617,
        satellite=False
    )

    planet_2 = Planet(
        name="Venus",
        description="Second planet in the solar system",
        color="yellow",
        size=7520,
        satellite=False
    )

    db.session.add_all([planet_1, planet_2])
    db.session.commit()
