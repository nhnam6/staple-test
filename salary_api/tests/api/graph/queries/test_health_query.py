import unittest

import graphene

from api.graph.queries.health_query import HealthQuery


class TestHealthQuery(unittest.TestCase):
    """Unit test for the HealthQuery GraphQL resolver."""

    def setUp(self):
        """Set up the GraphQL schema with the HealthQuery."""
        # Create a schema for testing with the HealthQuery
        self.schema = graphene.Schema(query=HealthQuery)

    def test_health_query(self):
        """Test that the health query returns 'Ok'."""
        # Define the GraphQL query string
        query = """
        {
            health
        }
        """
        # Execute the query against the schema
        result = self.schema.execute(query)

        # Verify the result is as expected
        self.assertIsNone(result.errors)
        self.assertEqual(result.data["health"], "Ok")
