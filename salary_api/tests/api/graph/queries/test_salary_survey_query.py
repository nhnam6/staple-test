import unittest
from unittest.mock import (
    MagicMock,
    patch,
)

import graphene

from api.graph.queries.salary_survey_query import SalarySurveyQuery
from model.salary import SalarySurvey  # pylint: disable=unused-import


class TestSalarySurveyQuery(unittest.TestCase):
    """Unit tests for the SalarySurveyQuery GraphQL resolvers."""

    def setUp(self):
        """Set up the GraphQL schema with the SalarySurveyQuery."""
        self.schema = graphene.Schema(query=SalarySurveyQuery)

    @patch("api.graph.queries.salary_survey_query.fetch_data")
    @patch("api.graph.queries.salary_survey_query.get_es_client")
    def test_list_compensation(self, mock_get_es_client, mock_fetch_data):
        """Test the list_compensation query with mocked data."""
        # Mock Elasticsearch client and data fetching
        mock_es_client = MagicMock()
        mock_get_es_client.return_value = mock_es_client
        mock_fetch_data.return_value = [
            {
                "id": "1",
                "timestamp": 1633024800,
                "employment_details": {"employment_type": "Full-time"},
                "work_experience_details": {
                    "years_in_industry": {"min_years": 5, "max_years": 10}
                },
                "job_details": {"title": "Software Engineer"},
                "salary_details": {"annual_salary": 50000},
                "personal_details": {"age_group": {"min_age": 25, "max_age": 30}},
            },
            {
                "id": "2",
                "timestamp": 1633025800,
                "employment_details": {"employment_type": "Part-time"},
                "work_experience_details": {
                    "years_in_industry": {"min_years": 1, "max_years": 2}
                },
                "job_details": {"title": "Data Scientist"},
                "salary_details": {"annual_salary": 70000},
                "personal_details": {"age_group": {"min_age": 25, "max_age": 25}},
            },
        ]

        # Define the GraphQL query string
        query = """
        {
            listCompensation {
                id
                timestamp
                employmentDetails {
                    employmentType
                }
                workExperienceDetails {
                    yearsInIndustry {
                        minYears
                        maxYears
                    }
                }
                jobDetails {
                    title
                }
                salaryDetails {
                    annualSalary
                }
                personalDetails {
                    ageGroup {
                        minAge
                        maxAge
                    }
                }
            }
        }
        """
        # Execute the query against the schema
        result = self.schema.execute(query)

        # Verify the result is as expected
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data["listCompensation"]), 2)
        self.assertEqual(
            result.data["listCompensation"][0]["jobDetails"]["title"],
            "Software Engineer",
        )
        self.assertEqual(
            result.data["listCompensation"][0]["salaryDetails"]["annualSalary"], 50000
        )
        self.assertEqual(
            result.data["listCompensation"][1]["jobDetails"]["title"], "Data Scientist"
        )
        self.assertEqual(
            result.data["listCompensation"][1]["salaryDetails"]["annualSalary"], 70000
        )

    @patch("api.graph.queries.salary_survey_query.fetch_data_by_id")
    @patch("api.graph.queries.salary_survey_query.get_es_client")
    def test_fetch_compensation(self, mock_get_es_client, mock_fetch_data_by_id):
        """Test the fetch_compensation query with mocked data."""
        # Mock Elasticsearch client and data fetching by ID
        mock_es_client = MagicMock()
        mock_get_es_client.return_value = mock_es_client
        mock_fetch_data_by_id.return_value = [
            {
                "id": "1",
                "timestamp": 1633024800,
                "employment_details": {"employment_type": "Full-time"},
                "work_experience_details": {
                    "years_in_industry": {"min_years": 5, "max_years": 10}
                },
                "job_details": {"title": "Software Engineer"},
                "salary_details": {"annual_salary": 50000},
                "personal_details": {"age_group": {"min_age": 25, "max_age": 30}},
            },
        ]

        # Define the GraphQL query string
        query = """
        {
            fetchCompensation(id: "1") {
                id
                timestamp
                employmentDetails {
                    employmentType
                }
                workExperienceDetails {
                    yearsInIndustry {
                        minYears
                        maxYears
                    }
                }
                jobDetails {
                    title
                }
                salaryDetails {
                    annualSalary
                }
                personalDetails {
                    ageGroup {
                        minAge
                        maxAge
                    }
                }
            }
        }
        """
        # Execute the query against the schema
        result = self.schema.execute(query)

        # Verify the result is as expected
        self.assertIsNone(result.errors)
        self.assertEqual(
            result.data["fetchCompensation"]["jobDetails"]["title"], "Software Engineer"
        )
        self.assertEqual(
            result.data["fetchCompensation"]["salaryDetails"]["annualSalary"], 50000
        )
        self.assertEqual(
            result.data["fetchCompensation"]["personalDetails"]["ageGroup"]["minAge"],
            25,
        )
        self.assertEqual(
            result.data["fetchCompensation"]["personalDetails"]["ageGroup"]["maxAge"],
            30,
        )

    @patch("api.graph.queries.salary_survey_query.fetch_data_by_id")
    @patch("api.graph.queries.salary_survey_query.get_es_client")
    def test_fetch_compensation_not_found(
        self, mock_get_es_client, mock_fetch_data_by_id
    ):
        """Test the fetch_compensation query when the record is not found."""
        # Mock Elasticsearch client and data fetching by ID
        mock_es_client = MagicMock()
        mock_get_es_client.return_value = mock_es_client
        mock_fetch_data_by_id.return_value = []  # Simulate no data found

        # Define the GraphQL query string
        query = """
        {
            fetchCompensation(id: "1") {
                id
                timestamp
                employmentDetails {
                    employmentType
                }
                workExperienceDetails {
                    yearsInIndustry {
                        minYears
                        maxYears
                    }
                }
                jobDetails {
                    title
                }
                salaryDetails {
                    annualSalary
                }
                personalDetails {
                    ageGroup {
                        minAge
                        maxAge
                    }
                }
            }
        }
        """
        # Execute the query against the schema
        result = self.schema.execute(query)

        # Verify the result is None
        self.assertIsNone(result.errors)
        self.assertIsNone(result.data["fetchCompensation"])
