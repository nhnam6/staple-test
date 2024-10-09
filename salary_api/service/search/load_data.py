import json

import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import (
    BulkIndexError,
    bulk,
)

from logger.logger import logger


def prepare_data_for_indexing(df: pd.DataFrame) -> pd.DataFrame:
    df["age_group"] = df.apply(
        lambda x: {"gte": x["min_age"], "lte": x["max_age"]}, axis=1
    )
    df["work_experience"] = df.apply(
        lambda x: {"gte": x["min_years"], "lte": x["max_years"]}, axis=1
    )
    df = df.drop(columns=["min_age", "max_age", "min_years", "max_years"])
    return df


def index_data_to_elasticsearch(
    es_client: Elasticsearch,
    data: list[dict],
    index_name: str,
) -> None:
    # Prepare actions for the bulk API
    actions = [
        {
            "_index": index_name,
            "_source": json.dumps(doc),  # Ensure the document is JSON serializable
        }
        for doc in data
    ]

    try:
        success, _ = bulk(es_client, actions, stats_only=True)
        logger.info("Successfully indexed %s documents to %s", success, index_name)
    except BulkIndexError as e:
        # Log the errors
        for error in e.errors:
            logger.error(error)
