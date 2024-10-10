import unittest

from flask import Flask

from api.rest.healthcheck.routes import health


class TestHealthCheckRoute(unittest.TestCase):
    """Unit tests for the /health route."""

    def setUp(self):
        """Set up the Flask test client with the health blueprint."""
        app = Flask(__name__)
        app.register_blueprint(health)
        self.client = app.test_client()  # Create a test client

    def test_health_route(self):
        """Test if the /health endpoint returns a 200 status code and correct message."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Ok"})
