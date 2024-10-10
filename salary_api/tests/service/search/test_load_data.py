import unittest
from unittest.mock import (
    MagicMock,
    patch,
)

import pandas as pd  # pylint: disable=unused-import
from elasticsearch import Elasticsearch
from elasticsearch.helpers import BulkIndexError

from service.search.load_data import index_data_to_elasticsearch


class TestLoadData(unittest.TestCase):
    """Unit tests for data preparation and indexing functions."""

    @patch("service.search.load_data.bulk")
    @patch("service.search.load_data.logger")
    def test_index_data_to_elasticsearch_success(self, mock_logger, mock_bulk):
        """Test successful indexing of data to Elasticsearch."""
        # Mock the bulk function to simulate successful indexing
        mock_bulk.return_value = (2, [])

        # Sample data for indexing
        es_client = MagicMock(Elasticsearch)
        data = [
            {"field1": "value1", "field2": "value2"},
            {"field1": "value3", "field2": "value4"},
        ]
        index_name = "test-index"

        # Call the function
        index_data_to_elasticsearch(es_client, data, index_name)

        # Verify that bulk was called with the correct arguments
        actions = [
            {
                "_index": index_name,
                "_source": '{"field1": "value1", "field2": "value2"}',
            },
            {
                "_index": index_name,
                "_source": '{"field1": "value3", "field2": "value4"}',
            },
        ]
        mock_bulk.assert_called_once_with(es_client, actions, stats_only=True)

        # Verify the logger was called to confirm successful indexing
        mock_logger.info.assert_called_once_with(
            "Successfully indexed %s documents to %s", 2, index_name
        )

    @patch("service.search.load_data.bulk")
    @patch("service.search.load_data.logger")
    def test_index_data_to_elasticsearch_bulk_index_error(self, mock_logger, mock_bulk):
        """Test handling of BulkIndexError during indexing."""
        # Simulate a BulkIndexError
        mock_bulk.side_effect = BulkIndexError(
            "Bulk indexing error", errors=["error1", "error2"]
        )

        # Sample data for indexing
        es_client = MagicMock(Elasticsearch)
        data = [{"field1": "value1", "field2": "value2"}]
        index_name = "test-index"

        # Call the function
        index_data_to_elasticsearch(es_client, data, index_name)

        # Verify that the errors were logged
        mock_logger.error.assert_any_call("error1")
        mock_logger.error.assert_any_call("error2")
