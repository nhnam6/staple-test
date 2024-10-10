import unittest

from service.data_transformation.heplers import (
    parse_salary,
    split_range,
    split_work_experience,
)


class TestHelpers(unittest.TestCase):
    """Unit tests for helper functions in helpers.py."""

    def test_parse_salary(self):
        """Test parsing salary strings with various formats."""
        # Test with plain numbers
        self.assertEqual(parse_salary("50000"), 50000)
        self.assertEqual(parse_salary("1234.56"), 1234.56)

        # Test with commas
        self.assertEqual(parse_salary("50,000"), 50000)
        self.assertEqual(parse_salary("1,234,567"), 1234567)

        # Test with 'k' for thousands
        self.assertEqual(parse_salary("50k"), 50000)
        self.assertEqual(parse_salary("1.5k"), 1500)

        # Test with 'm' for millions
        self.assertEqual(parse_salary("1m"), 1000000)
        self.assertEqual(parse_salary("2.3m"), 2300000)

        # Test with invalid values
        self.assertEqual(parse_salary("not a number"), 0)
        self.assertEqual(parse_salary(None), 0)
        self.assertEqual(parse_salary(""), 0)

    def test_split_range(self):
        """Test splitting a range string into two integers."""
        # Test valid ranges
        self.assertEqual(split_range("25-34"), (25, 34))
        self.assertEqual(split_range("1-100"), (1, 100))

        # Test invalid ranges
        self.assertEqual(split_range("not a range"), (0, 0))
        self.assertEqual(split_range("123"), (0, 0))
        self.assertEqual(split_range(""), (0, 0))

    def test_split_work_experience(self):
        """Test splitting work experience strings."""
        # Test ranges
        self.assertEqual(split_work_experience("3-5 years"), (3, 5))
        self.assertEqual(split_work_experience("10-15 years"), (10, 15))

        # Test special cases
        self.assertEqual(split_work_experience("Less than 1 year"), (0, 1))
        self.assertEqual(split_work_experience("More than 50 years"), (50, 100))
        self.assertEqual(split_work_experience("5+ years"), (5, 100))

        # Test single number
        self.assertEqual(split_work_experience("3 years"), (3, 3))

        # Test invalid cases
        self.assertEqual(split_work_experience("not a valid experience"), (0, 0))
        self.assertEqual(split_work_experience(""), (0, 0))
