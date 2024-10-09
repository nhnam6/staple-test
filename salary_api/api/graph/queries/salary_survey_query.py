import graphene

from config import Config
from infra.es_client import get_es_client
from model.salary import SalarySurvey
from service.search.fetch_data import (
    fetch_data,
    fetch_data_by_id,
)


class SalarySurveyQuery(graphene.ObjectType):
    # Query to list compensation data with filtering and sorting
    list_compensation = graphene.List(
        SalarySurvey,
        salary_gte=graphene.Float(description="Minimum salary filter"),
        salary_lte=graphene.Float(description="Maximum salary filter"),
        sort_by=graphene.String(
            description="Field to sort by, prefix with - for descending"
        ),
    )

    # Query to fetch a single record
    fetch_compensation = graphene.Field(
        SalarySurvey,
        id=graphene.String(required=True),
    )

    def resolve_list_compensation(
        self,
        info,
        salary_gte=None,
        salary_lte=None,
        sort_by=None,
    ):  # pylint: disable=unused-argument

        # Query to list compensation data with filtering and sorting
        es_client = get_es_client(Config.ELASTICSEARCH_URL)
        data = fetch_data(
            es_client=es_client,
            index_name=Config.ELASTICSEARCH_SALARY_INDEX,
            salary_gte=salary_gte,
            salary_lte=salary_lte,
            sort_by=sort_by,
        )

        # Assuming SalarySurvey is a class that can deserialize data from Elasticsearch
        # and your fetch_data function directly returns data in a compatible format
        results = [SalarySurvey(**item) for item in data]
        return results

    def resolve_fetch_compensation(
        self,
        info,
        id,
    ):  # pylint: disable=unused-argument
        # Query to fetch a single record
        es_client = get_es_client(Config.ELASTICSEARCH_URL)
        data = fetch_data_by_id(
            es_client=es_client,
            index_name=Config.ELASTICSEARCH_SALARY_INDEX,
            doc_id=id,
        )
        if data:
            return SalarySurvey(**data[0])
        return None
