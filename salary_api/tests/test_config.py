import os
import unittest

from config import (
    Config,
    EnvironmentErr,
    get_env_value,
)


class TestConfig(unittest.TestCase):
    """Unit tests for the configuration module."""

    def test_get_env_value_existing(self):
        """Test if get_env_value returns the value of an existing environment variable."""
        os.environ["TEST_ENV_VAR"] = "test_value"
        self.assertEqual(get_env_value("TEST_ENV_VAR"), "test_value")

    def test_get_env_value_default(self):
        """Test if get_env_value returns the default value when the environment variable is not set."""
        self.assertEqual(
            get_env_value("NON_EXISTENT_VAR", "default_value"), "default_value"
        )

    def test_get_env_value_exception(self):
        """Test if get_env_value raises an EnvironmentErr when the environment variable is not set and no default is provided."""
        with self.assertRaises(EnvironmentErr):
            get_env_value("NON_EXISTENT_VAR")

    def test_config_values(self):
        """Test if the Config class has the correct default values."""
        self.assertEqual(
            Config.ELASTICSEARCH_SALARY_INDEX, "salary-survey-index-202410"
        )
        self.assertEqual(
            Config.ELASTICSEARCH_SALARY_TEMPLATE, "salary-survey-template-202410"
        )
        self.assertEqual(Config.ELASTICSEARCH_URL, "http://localhost:9200")

    def tearDown(self):
        """Clean up environment variables after each test."""
        if "TEST_ENV_VAR" in os.environ:
            del os.environ["TEST_ENV_VAR"]
