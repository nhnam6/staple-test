from config import Config
from infra.es_client import get_es_client
from logger.logger import logger
from service.search.index import (
    create_index,
    create_template,
)


def register_commands(app):
    @app.cli.group()
    def elasticsearch():
        pass

    @elasticsearch.command("create-index")
    def create_es_index():
        logger.info("Creating Elasticsearch index...")
        # Initialize Elasticsearch client
        es = get_es_client(Config.ELASTICSEARCH_URL)
        create_template(
            es,
            Config.ELASTICSEARCH_SALARY_TEMPLATE,
            [Config.ELASTICSEARCH_SALARY_INDEX],
        )

        create_index(es, Config.ELASTICSEARCH_SALARY_INDEX)
