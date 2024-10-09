from elasticsearch import Elasticsearch


def get_es_client(hosts: list[str]) -> Elasticsearch:
    # Initialize Elasticsearch client
    es = Elasticsearch(hosts=hosts)
    return es
