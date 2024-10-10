import unittest
from unittest.mock import (
    MagicMock,
    patch,
)

from service.search.index import (
    create_index,
    create_template,
)


class TestElasticsearchOperations(unittest.TestCase):
    """Unit tests for Elasticsearch index and template operations."""

    @patch("service.search.index.logger")
    def test_create_template(self, mock_logger):
        """Test creating or updating an Elasticsearch template."""
        # Mock Elasticsearch client
        mock_es = MagicMock()
        mock_es.indices.put_template.return_value = {"acknowledged": True}

        # Define test inputs
        template_name = "test_template"
        indexes = ["test-index-*"]

        # Call the create_template function
        create_template(mock_es, template_name, indexes)

        # Verify that put_template was called with the correct arguments
        mock_es.indices.put_template.assert_called_once()
        _, kwargs = mock_es.indices.put_template.call_args
        self.assertEqual(kwargs["name"], template_name)
        self.assertIn("index_patterns", kwargs["body"])
        self.assertEqual(kwargs["body"]["index_patterns"], indexes)
        self.assertIn("mappings", kwargs["body"])

        # Verify the logger was called to indicate the template was created/updated
        mock_logger.info.assert_called_once_with(
            "Template %s created/updated", template_name
        )

    @patch("service.search.index.logger")
    def test_create_index(self, mock_logger):
        """Test creating an Elasticsearch index if it does not exist."""
        # Mock Elasticsearch client
        mock_es = MagicMock()

        # Case 1: Index does not exist
        mock_es.indices.exists.return_value = False
        mock_es.indices.create.return_value = {"acknowledged": True}

        index_name = "test-index"
        create_index(mock_es, index_name)

        # Verify that the index was created
        mock_es.indices.create.assert_called_once_with(index=index_name)
        mock_logger.info.assert_called_with("Index %s created", index_name)

        # Case 2: Index already exists
        mock_es.indices.exists.return_value = True
        mock_es.indices.create.reset_mock()
        mock_logger.reset_mock()

        create_index(mock_es, index_name)

        # Verify that the index was not created but a log message was written
        mock_es.indices.create.assert_not_called()
        mock_logger.info.assert_called_with("Index %s already exists", index_name)
