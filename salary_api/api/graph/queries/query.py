from .health_query import HealthQuery
from .salary_survey_query import SalarySurveyQuery


class Query(
    HealthQuery,
    SalarySurveyQuery,
):
    pass
