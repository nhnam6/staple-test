from elasticsearch import Elasticsearch

from logger.logger import logger


def fetch_data(
    es_client: Elasticsearch,
    index_name: str,
    salary_gte=None,
    salary_lte=None,
    sort_by=None,
):

    # Query to list compensation data with filtering and sorting
    logger.debug(
        "Fetching data from index: %s with filters: %s, %s and sort_by: %s",
        index_name,
        salary_gte,
        salary_lte,
        sort_by,
    )
    query = {
        "query": {"bool": {"must": [], "filter": []}},
    }

    # Add salary range filters if specified
    if salary_gte is not None:
        query["query"]["bool"]["filter"].append(
            {"range": {"salary_details.annual_salary": {"gte": salary_gte}}}
        )

    if salary_lte is not None:
        query["query"]["bool"]["filter"].append(
            {"range": {"salary_details.annual_salary": {"lte": salary_lte}}}
        )

    # Add sorting if specified
    if sort_by:
        query["sort"] = [
            (
                {sort_by: {"order": "asc"}}
                if not sort_by.startswith("-")
                else {sort_by[1:]: {"order": "desc"}}
            )
        ]
    logger.debug("Query: %s", query)
    # Execute the query
    response = es_client.search(index=index_name, body=query)

    # Process the response and return the data
    data = []
    for hit in response["hits"]["hits"]:
        document_id = hit["_id"]  # Get the Elasticsearch document ID
        document = hit["_source"]
        document["id"] = document_id
        data.append(document)
    logger.debug("Data: %s", data)
    return data


def fetch_data_by_id(
    es_client: Elasticsearch,
    index_name: str,
    doc_id: str,
):
    logger.debug(
        "Fetching data from index: %s with ID: %s",
        index_name,
        doc_id,
    )
    # Query to fetch a single record
    query = {
        "query": {"match": {"_id": doc_id}},
    }
    response = es_client.search(index=index_name, body=query)

    # Process the response and return the data
    data = []
    for hit in response["hits"]["hits"]:
        document_id = hit["_id"]  # Get the Elasticsearch document ID
        document = hit["_source"]
        document["id"] = document_id
        data.append(document)
    logger.debug("Data: %s", data)
    return data
