import unittest

from flask import Flask

from app import create_app


class TestAppCreation(unittest.TestCase):
    """Unit test for the Flask application defined in app.py."""

    def setUp(self):
        """Set up the test client for the Flask app."""
        self.app = create_app()  # Create an instance of the Flask app
        self.client = self.app.test_client()  # Set up the test client

    def test_app_instance(self):
        """Test if the app instance is created successfully."""
        self.assertIsInstance(self.app, Flask)

    def test_healthcheck_route(self):
        """Test if the health check route is registered and returns 200."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_logger_setup(self):
        """Test if the logger is attached to the app."""
        self.assertIn("root", [h.name for h in self.app.logger.handlers])

    def test_graphql_endpoint(self):
        """Test if the GraphQL endpoint is registered and can handle a simple query."""
        # Perform a POST request with a simple GraphQL query
        query = '{"query": "{ __schema { queryType { name } } }"}'
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/graphql", data=query, headers=headers)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the response contains expected data
        self.assertIn(b"__schema", response.data)

    def test_commands_registered(self):
        """Test if the CLI commands are registered with the app."""
        commands = self.app.cli.list_commands(self.app)
        self.assertIn("elasticsearch", commands)
        self.assertIn("load-salary", commands)
