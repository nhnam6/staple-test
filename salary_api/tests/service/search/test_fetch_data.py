import unittest
from unittest.mock import (
    MagicMock,
    patch,
)

from service.search.fetch_data import (
    fetch_data,
    fetch_data_by_id,
)


class TestFetchData(unittest.TestCase):
    """Unit tests for the data fetching functions."""

    @patch("service.search.fetch_data.logger")
    def test_fetch_data(self, mock_logger):  #  pylint: disable=unused-argument
        """Test fetching data with filters and sorting from Elasticsearch."""
        # Mock Elasticsearch client
        mock_es_client = MagicMock()
        mock_es_client.search.return_value = {
            "hits": {
                "hits": [
                    {
                        "_id": "1",
                        "_source": {"salary_details": {"annual_salary": 50000}},
                    },
                    {
                        "_id": "2",
                        "_source": {"salary_details": {"annual_salary": 70000}},
                    },
                ]
            }
        }

        # Call fetch_data with test filters
        index_name = "test-index"
        salary_gte = 40000
        salary_lte = 80000
        sort_by = "-salary_details.annual_salary"
        result = fetch_data(mock_es_client, index_name, salary_gte, salary_lte, sort_by)

        # Verify the Elasticsearch search was called with the correct query
        expected_query = {
            "query": {
                "bool": {
                    "must": [],
                    "filter": [
                        {"range": {"salary_details.annual_salary": {"gte": 40000}}},
                        {"range": {"salary_details.annual_salary": {"lte": 80000}}},
                    ],
                }
            },
            "sort": [{"salary_details.annual_salary": {"order": "desc"}}],
        }
        mock_es_client.search.assert_called_once_with(
            index=index_name, body=expected_query
        )

        # Verify the result matches the expected processed data
        expected_result = [
            {"id": "1", "salary_details": {"annual_salary": 50000}},
            {"id": "2", "salary_details": {"annual_salary": 70000}},
        ]
        self.assertEqual(result, expected_result)

    @patch("service.search.fetch_data.logger")
    def test_fetch_data_by_id(self, mock_logger):  # pylint: disable=unused-argument
        """Test fetching a single document by ID from Elasticsearch."""
        # Mock Elasticsearch client
        mock_es_client = MagicMock()
        mock_es_client.search.return_value = {
            "hits": {
                "hits": [
                    {
                        "_id": "1",
                        "_source": {"salary_details": {"annual_salary": 60000}},
                    }
                ]
            }
        }

        # Call fetch_data_by_id with a test ID
        index_name = "test-index"
        doc_id = "1"
        result = fetch_data_by_id(mock_es_client, index_name, doc_id)

        # Verify the Elasticsearch search was called with the correct query
        expected_query = {"query": {"match": {"_id": doc_id}}}
        mock_es_client.search.assert_called_once_with(
            index=index_name, body=expected_query
        )

        # Verify the result matches the expected processed data
        expected_result = [{"id": "1", "salary_details": {"annual_salary": 60000}}]
        self.assertEqual(result, expected_result)

    @patch("service.search.fetch_data.logger")
    def test_fetch_data_no_results(
        self, mock_logger
    ):  # pylint: disable=unused-argument
        """Test fetching data returns an empty list when no results are found."""
        # Mock Elasticsearch client
        mock_es_client = MagicMock()
        mock_es_client.search.return_value = {"hits": {"hits": []}}

        # Call fetch_data with no filters to simulate no matching documents
        index_name = "test-index"
        result = fetch_data(mock_es_client, index_name)

        # Verify that the result is an empty list
        self.assertEqual(result, [])

    @patch("service.search.fetch_data.logger")
    def test_fetch_data_by_id_no_results(
        self, mock_logger
    ):  # pylint: disable=unused-argument
        """Test fetching data by ID returns an empty list when no matching document is found."""
        # Mock Elasticsearch client
        mock_es_client = MagicMock()
        mock_es_client.search.return_value = {"hits": {"hits": []}}

        # Call fetch_data_by_id with a non-existent ID
        index_name = "test-index"
        doc_id = "nonexistent-id"
        result = fetch_data_by_id(mock_es_client, index_name, doc_id)

        # Verify that the result is an empty list
        self.assertEqual(result, [])
