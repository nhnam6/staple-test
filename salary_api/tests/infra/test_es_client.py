import unittest
from unittest.mock import (
    MagicMock,
    patch,
)

from elasticsearch import Elasticsearch

from infra.es_client import get_es_client


class TestEsClient(unittest.TestCase):
    """Unit tests for the Elasticsearch client initialization."""

    @patch("infra.es_client.Elasticsearch")
    def test_get_es_client(self, mock_elasticsearch):
        """Test that get_es_client correctly initializes the Elasticsearch client."""
        # Mock the return value for the Elasticsearch initialization
        mock_es_instance = MagicMock(Elasticsearch)
        mock_elasticsearch.return_value = mock_es_instance

        # Test inputs
        hosts = ["http://localhost:9200", "http://otherhost:9200"]

        # Call the function
        es_client = get_es_client(hosts)

        # Verify that Elasticsearch was initialized with the correct hosts
        mock_elasticsearch.assert_called_once_with(hosts=hosts)

        # Verify that the returned client is the mocked instance
        self.assertEqual(es_client, mock_es_instance)
