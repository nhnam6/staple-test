import unittest

from flask import Flask

from main import app  # Import the app instance from main.py


class TestMainApp(unittest.TestCase):
    """Unit test for the Flask application defined in main.py."""

    def setUp(self):
        """Set up the test client for the Flask app."""
        self.app = app.test_client()  # Create a test client
        self.app.testing = True  # Enable testing mode

    def test_app_creation(self):
        """Test if the app instance is created successfully."""
        self.assertIsNotNone(app)
        assert isinstance(app, Flask)
