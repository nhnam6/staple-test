import os


class EnvironmentErr(Exception):
    pass


def get_env_value(env_name: str, default: str | None = None) -> str:
    """
    Functions is used to get value from environment.
    Raise Exception when the value not found
    Args:
        env_name (str): the environment name
        default (str): the default value
    Returns:
        str: the value of environment
    """
    try:
        value = os.environ[env_name]
    except KeyError as ex:
        if default is None:
            raise EnvironmentErr(
                "Trying to get an undefined environment variable"
            ) from ex
        value = default

    return value


class Config:
    ELASTICSEARCH_SALARY_INDEX = "salary-survey-index-202410"
    ELASTICSEARCH_SALARY_TEMPLATE = "salary-survey-template-202410"
    ELASTICSEARCH_URL = get_env_value("ELASTICSEARCH_URL", "http://localhost:9200")
