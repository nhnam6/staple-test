import click
import pandas as pd

from config import Config
from infra.es_client import get_es_client
from logger.logger import logger
from service.data_transformation.clean_salary_survey_1 import (
    clean_and_transform_survey as clean_and_transform_survey_1,
)
from service.data_transformation.clean_salary_survey_2 import (
    clean_and_transform_survey as clean_and_transform_survey_2,
)
from service.data_transformation.clean_salary_survey_3 import (
    clean_and_transform_survey as clean_and_transform_survey_3,
)
from service.data_transformation.trans_salary_survey_1 import (
    prepare_data_for_indexing as prepare_data_for_indexing_survey_1,
)
from service.data_transformation.trans_salary_survey_2 import (
    prepare_data_for_indexing as prepare_data_for_indexing_survey_2,
)
from service.data_transformation.trans_salary_survey_3 import (
    prepare_data_for_indexing as prepare_data_for_indexing_survey_3,
)
from service.search.load_data import index_data_to_elasticsearch


def register_commands(app):
    @app.cli.group()
    def load_salary():
        pass

    @load_salary.command("survey-1")
    @click.argument("file_path")
    def load_survey_1_csv(file_path):
        logger.info("Loading salary data from CSV %s ...", file_path)
        data_frame = pd.read_csv(file_path)

        logger.info("Cleaning and transforming data ...")
        df_cleaned = clean_and_transform_survey_1(data_frame)
        data = prepare_data_for_indexing_survey_1(df_cleaned)

        es_client = get_es_client([Config.ELASTICSEARCH_URL])
        logger.info("Indexing data to Elasticsearch ...")
        index_data_to_elasticsearch(es_client, data, Config.ELASTICSEARCH_SALARY_INDEX)
        logger.info("Data has been indexed to Elasticsearch successfully.")

    @load_salary.command("survey-2")
    @click.argument("file_path")
    def load_survey_2_csv(file_path):
        logger.info("Loading salary data from CSV %s ...", file_path)
        data_frame = pd.read_csv(file_path)

        logger.info("Cleaning and transforming data ...")
        df_cleaned = clean_and_transform_survey_2(data_frame)
        data = prepare_data_for_indexing_survey_2(df_cleaned)

        es_client = get_es_client([Config.ELASTICSEARCH_URL])
        logger.info("Indexing data to Elasticsearch ...")
        index_data_to_elasticsearch(es_client, data, Config.ELASTICSEARCH_SALARY_INDEX)
        logger.info("Data has been indexed to Elasticsearch successfully.")

    @load_salary.command("survey-3")
    @click.argument("file_path")
    def load_survey_3_csv(file_path):
        logger.info("Loading salary data from CSV %s ...", file_path)
        data_frame = pd.read_csv(file_path)

        logger.info("Cleaning and transforming data ...")
        df_cleaned = clean_and_transform_survey_3(data_frame)
        data = prepare_data_for_indexing_survey_3(df_cleaned)

        es_client = get_es_client([Config.ELASTICSEARCH_URL])
        logger.info("Indexing data to Elasticsearch ...")
        index_data_to_elasticsearch(es_client, data, Config.ELASTICSEARCH_SALARY_INDEX)
        logger.info("Data has been indexed to Elasticsearch successfully.")
