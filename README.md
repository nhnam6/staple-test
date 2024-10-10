# Staple Test

## Approach

Here's an explanation of the approach to implementing a project that uses technologies like Flask for the API, Elasticsearch for search capabilities, Docker and Docker Compose for containerization, unit testing, ETL data processing, and designing Elasticsearch index templates.

### API Implementation with Flask

1. Flask as the Web Framework: Flask is a lightweight and flexible Python web framework. It is well-suited for building RESTful APIs because of its simplicity and modularity.
2. GraphQL and REST Endpoints: The API is designed to support both GraphQL and RESTful access patterns, allowing users to choose between flexible queries with GraphQL and traditional REST endpoints.
3. API Structure: The Flask application is structured in a modular way, with separate directories for GraphQL queries, REST routes, service logic, and CLI commands. This separation of concerns improves maintainability and readability.

### Data Storage and Search with Elasticsearch

1. Elasticsearch as the Primary Data Store: Elasticsearch is used for storing and querying data due to its powerful full-text search capabilities and support for aggregations. It allows the API to perform efficient searches, aggregations, and filtering of large datasets.
2. Index Design and Template: The index mapping is carefully designed, choosing appropriate data types for each field. For example:
   Text fields are indexed as text with keyword sub-fields for exact matches.
   Numeric fields (e.g., salaries) use types like float for precision.
   Nested fields are used for complex data structures, such as historical salary data.
3. Index Templates: Index templates are created to define index settings and mappings. This ensures that new indices created in the future automatically follow the predefined structure, making data consistent across indices.

### Containerization with Docker and Orchestration with Docker Compose

1. Dockerizing the Application: Each component of the application, including the Flask API, Elasticsearch, and Kibana, is containerized using Docker. This ensures that the application can run consistently across different environments.
2. Using Docker Compose for Multi-Service Management: Docker Compose is used to orchestrate multiple containers, such as the Flask API, Elasticsearch, and Kibana, making it easy to set up and manage the development environment.

### ETL Data Processing

1. Extract, Transform, Load (ETL) Pipeline: An ETL pipeline is used to load data from various sources (e.g., CSV files) into Elasticsearch. The data is cleaned and transformed before being indexed.
2. Automating Data Loading with CLI Commands: CLI commands are created to automate the process of loading salary survey data into Elasticsearch. This helps ensure that data is consistently processed and indexed.

## Overview

Provide a brief description of what the project does and the problem it solves.

## Prerequisites

Before you begin, ensure you have installed the following on your development machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

These instructions will cover usage information and for the docker container

### Configuration

Explain how to configure the environment variables if necessary:

1. Copy the sample environment configuration file:

   ```bash
   cp .sample.env .env
   ```

2. Modify the .env file according to your needs.

## Using Docker Compose

1. Building services

```
docker-compose up --build
```

2. Start services in the background

```
docker-compose up -d
```

3. List services

```
docker compose ps
```

Example output:

```
NAME                                 IMAGE                                                 COMMAND                  SERVICE                CREATED              STATUS              PORTS
staple-test-es-1                     docker.elastic.co/elasticsearch/elasticsearch:8.7.1   "/bin/tini -- /usr/l…"   es                     2 days ago           Up 4 hours          0.0.0.0:9200->9200/tcp, 9300/tcp
staple-test-kibana-1                 docker.elastic.co/kibana/kibana:8.7.1                 "/bin/tini -- /usr/l…"   kibana                 2 days ago           Up 4 hours          0.0.0.0:5601->5601/tcp
staple-test-salary-survey-server-1   staple-test-salary-survey-server                      "pipenv run runserver"   salary-survey-server   About a minute ago   Up About a minute   0.0.0.0:5001->5000/tcp
```

4. Viewing output

```
docker compose logs -f --tail 100 salary-survey-server
```

Example log:

```
alary_survey_server-1  |  * Serving Flask app 'main.py'
salary-survey-server-1  |  * Debug mode: on
salary-survey-server-1  | 2024-10-09 19:13:14,806 - INFO - werkzeug - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
salary-survey-server-1  |  * Running on all addresses (0.0.0.0)
salary-survey-server-1  |  * Running on http://127.0.0.1:5000
salary-survey-server-1  |  * Running on http://172.22.0.4:5000
salary-survey-server-1  | 2024-10-09 19:13:14,806 - INFO - werkzeug - Press CTRL+C to quit
salary-survey-server-1  | 2024-10-09 19:13:14,807 - INFO - werkzeug -  * Restarting with stat
salary-survey-server-1  | 2024-10-09 19:13:16,406 - WARNING - werkzeug -  * Debugger is active!
salary-survey-server-1  | 2024-10-09 19:13:16,409 - INFO - werkzeug -  * Debugger PIN: 732-871-805`
```

5. Healthcheck API

```
GET http://127.0.0.1:5001/health
```

6. Create index

```bash
docker compose run -it salary-survey-server pipenv run flask elasticsearch create-index
```

Example output

```
 ✔ Container staple_test-es-1  Running                                                                                                                                                                                                                                                           0.0s
2024-10-10 03:28:20,259 - INFO - root - Creating Elasticsearch index...
2024-10-10 03:28:20,275 - DEBUG - urllib3.connectionpool - Starting new HTTP connection (1): es:9200
2024-10-10 03:28:21,272 - DEBUG - urllib3.connectionpool - http://es:9200 "PUT /_template/salary-survey-template-202410 HTTP/11" 200 0
2024-10-10 03:28:21,272 - INFO - elastic_transport.transport - PUT http://es:9200/_template/salary-survey-template-202410 [status:200 duration:0.998s]
/code/service/search/index.py:90: ElasticsearchWarning: Legacy index templates are deprecated in favor of composable templates.
  es.indices.put_template(
2024-10-10 03:28:21,460 - INFO - root - Template salary-survey-template-202410 created/updated
2024-10-10 03:28:21,468 - DEBUG - urllib3.connectionpool - http://es:9200 "HEAD /salary-survey-index-202410 HTTP/11" 200 0
2024-10-10 03:28:21,469 - INFO - elastic_transport.transport - HEAD http://es:9200/salary-survey-index-202410 [status:200 duration:0.008s]
2024-10-10 03:28:21,469 - INFO - root - Index salary-survey-index-202410 already exists
```

7. Load data

```bash
# survey 1
docker compose run -it salary-survey-server pipenv run flask load-salary survey-1 data/salary_survey-1.csv

# survey 2
docker compose run -it salary-survey-server pipenv run flask load-salary survey-2 data/salary_survey-2.csv

# survey 3
docker compose run -it salary-survey-server pipenv run flask load-salary survey-3 data/salary_survey-3.csv

```

## Exercise

1. Exercise A: https://github.com/nhnam6/staple-test/blob/main/docs/Exercise-A/README.md

2. Exercise B: https://github.com/nhnam6/staple-test/blob/main/docs/Exercise-B/README.md

## Unittest

Ref: https://github.com/nhnam6/staple-test/blob/main/salary_api/README.md

Unittest

```
collected 27 items

tests/api/graph/queries/test_health_query.py::TestHealthQuery::test_health_query PASSED                                                                                                                [  3%]
tests/api/graph/queries/test_salary_survey_query.py::TestSalarySurveyQuery::test_fetch_compensation PASSED                                                                                             [  7%]
tests/api/graph/queries/test_salary_survey_query.py::TestSalarySurveyQuery::test_fetch_compensation_not_found PASSED                                                                                   [ 11%]
tests/api/graph/queries/test_salary_survey_query.py::TestSalarySurveyQuery::test_list_compensation PASSED                                                                                              [ 14%]
tests/api/rest/test_healthcheck.py::TestHealthCheckRoute::test_health_route PASSED                                                                                                                     [ 18%]
tests/infra/test_es_client.py::TestEsClient::test_get_es_client PASSED                                                                                                                                 [ 22%]
tests/service/data_transformation/test_helpers.py::TestHelpers::test_parse_salary PASSED                                                                                                               [ 25%]
tests/service/data_transformation/test_helpers.py::TestHelpers::test_split_range PASSED                                                                                                                [ 29%]
tests/service/data_transformation/test_helpers.py::TestHelpers::test_split_work_experience PASSED                                                                                                      [ 33%]
tests/service/search/test_fetch_data.py::TestFetchData::test_fetch_data PASSED                                                                                                                         [ 37%]
tests/service/search/test_fetch_data.py::TestFetchData::test_fetch_data_by_id PASSED                                                                                                                   [ 40%]
tests/service/search/test_fetch_data.py::TestFetchData::test_fetch_data_by_id_no_results PASSED                                                                                                        [ 44%]
tests/service/search/test_fetch_data.py::TestFetchData::test_fetch_data_no_results PASSED                                                                                                              [ 48%]
tests/service/search/test_index.py::TestElasticsearchOperations::test_create_index PASSED                                                                                                              [ 51%]
tests/service/search/test_index.py::TestElasticsearchOperations::test_create_template PASSED                                                                                                           [ 55%]
tests/service/search/test_load_data.py::TestLoadData::test_index_data_to_elasticsearch_bulk_index_error PASSED                                                                                         [ 59%]
tests/service/search/test_load_data.py::TestLoadData::test_index_data_to_elasticsearch_success PASSED                                                                                                  [ 62%]
tests/test_app.py::TestAppCreation::test_app_instance PASSED                                                                                                                                           [ 66%]
tests/test_app.py::TestAppCreation::test_commands_registered PASSED                                                                                                                                    [ 70%]
tests/test_app.py::TestAppCreation::test_graphql_endpoint PASSED                                                                                                                                       [ 74%]
tests/test_app.py::TestAppCreation::test_healthcheck_route PASSED                                                                                                                                      [ 77%]
tests/test_app.py::TestAppCreation::test_logger_setup PASSED                                                                                                                                           [ 81%]
tests/test_config.py::TestConfig::test_config_values PASSED                                                                                                                                            [ 85%]
tests/test_config.py::TestConfig::test_get_env_value_default PASSED                                                                                                                                    [ 88%]
tests/test_config.py::TestConfig::test_get_env_value_exception PASSED                                                                                                                                  [ 92%]
tests/test_config.py::TestConfig::test_get_env_value_existing PASSED                                                                                                                                   [ 96%]
tests/test_main.py::TestMainApp::test_app_creation PASSED                                                                                                                                              [100%]

============================================================================================= 27 passed in 1.72s =============================================================================================
```

if you want to run tests with a coverage report:

```
collected 27 items

tests/api/graph/queries/test_health_query.py .                                                                                                                                                         [  3%]
tests/api/graph/queries/test_salary_survey_query.py ...                                                                                                                                                [ 14%]
tests/api/rest/test_healthcheck.py .                                                                                                                                                                   [ 18%]
tests/infra/test_es_client.py .                                                                                                                                                                        [ 22%]
tests/service/data_transformation/test_helpers.py ...                                                                                                                                                  [ 33%]
tests/service/search/test_fetch_data.py ....                                                                                                                                                           [ 48%]
tests/service/search/test_index.py ..                                                                                                                                                                  [ 55%]
tests/service/search/test_load_data.py ..                                                                                                                                                              [ 62%]
tests/test_app.py .....                                                                                                                                                                                [ 81%]
tests/test_config.py ....                                                                                                                                                                              [ 96%]
tests/test_main.py .                                                                                                                                                                                   [100%]

---------- coverage: platform darwin, python 3.12.4-final-0 ----------
Name                                                   Stmts   Miss  Cover
--------------------------------------------------------------------------
api/__init__.py                                            0      0   100%
api/graph/__init__.py                                      0      0   100%
api/graph/queries/__init__.py                              0      0   100%
api/graph/queries/health_query.py                          5      0   100%
api/graph/queries/query.py                                 4      0   100%
api/graph/queries/salary_survey_query.py                  19      0   100%
api/rest/__init__.py                                       0      0   100%
api/rest/healthcheck/routes.py                             5      0   100%
app.py                                                    19      0   100%
cli/__init__.py                                            0      0   100%
cli/elasticsearch_cmd.py                                  14      5    64%
cli/load_salary_survey_cmd.py                             52     28    46%
config.py                                                 15      0   100%
infra/es_client.py                                         4      0   100%
logger/__init__.py                                         0      0   100%
logger/logger.py                                           7      0   100%
main.py                                                    2      0   100%
model/salary.py                                           62      0   100%
service/data_transformation/__init__.py                    0      0   100%
service/data_transformation/clean_salary_survey_1.py      24     21    12%
service/data_transformation/clean_salary_survey_2.py      43     39     9%
service/data_transformation/clean_salary_survey_3.py      27     24    11%
service/data_transformation/heplers.py                    36      0   100%
service/data_transformation/trans_salary_survey_1.py       7      5    29%
service/data_transformation/trans_salary_survey_2.py       7      5    29%
service/data_transformation/trans_salary_survey_3.py       7      5    29%
service/search/__init__.py                                 0      0   100%
service/search/fetch_data.py                              33      0   100%
service/search/index.py                                   11      0   100%
service/search/load_data.py                               13      0   100%
tests/__init__.py                                          0      0   100%
tests/api/__init__.py                                      0      0   100%
tests/api/graph/__init__.py                                0      0   100%
tests/api/graph/queries/__init__.py                        0      0   100%
tests/api/graph/queries/test_health_query.py              11      0   100%
tests/api/graph/queries/test_salary_survey_query.py       45      0   100%
tests/api/rest/__init__.py                                 0      0   100%
tests/api/rest/test_healthcheck.py                        12      0   100%
tests/infra/__init__.py                                    0      0   100%
tests/infra/test_es_client.py                             13      0   100%
tests/service/__init__.py                                  0      0   100%
tests/service/data_transformation/__init__.py              0      0   100%
tests/service/data_transformation/test_helpers.py         30      0   100%
tests/service/search/__init__.py                           0      0   100%
tests/service/search/test_fetch_data.py                   43      0   100%
tests/service/search/test_index.py                        33      0   100%
tests/service/search/test_load_data.py                    28      0   100%
tests/test_app.py                                         24      0   100%
tests/test_config.py                                      19      0   100%
tests/test_main.py                                        10      0   100%
--------------------------------------------------------------------------
TOTAL                                                    684    132    81%


============================================================================================= 27 passed in 4.94s =============================================================================================
```

## Project Directory Tree

```graphql
staple-test/
├── .vscode/                 # VSCode settings and configurations for the project environment
├── docs/                    # Documentation files for the project
├── salary_api/              # Main directory for the Salary API application
│   ├── api/
│   │   ├── graph/
│   │   │   └── queries/     # GraphQL queries
│   │   └── rest/            # REST API endpoints
│   ├── cli/
│   │   ├── elasticsearch_cmd.py  # CLI commands for Elasticsearch operations
│   │   └── load_salary_survey_cmd.py  # CLI command to load salary survey data
│   ├── data/                # Data files or resources used by the application
│   ├── infra/
│   │   └── es_client.py     # Elasticsearch client configuration
│   ├── logger/              # Logging configuration and setup
│   ├── service/
│   │   ├── search/          # Search services, possibly wrapping Elasticsearch queries
│   │   └── data_transformation/  # Services for data transformation tasks
│   ├── tests/               # Test suite for the application
│   ├── .dockerignore        # Specifies files to ignore in Docker builds
│   ├── .python-version      # Specifies Python version managed by pyenv
│   ├── app.py               # Flask application initialization
│   ├── main.py              # Main entry point for the Flask application
│   ├── config.py            # Configuration settings for the application
│   ├── Dockerfile           # Dockerfile for building the application container
│   ├── Pipfile              # Pipenv file for managing dependencies
│   ├── Pipfile.lock         # Lock file to ensure reproducible builds
│   ├── pyproject.yaml       # Python project settings including build system configuration
│   ├── README.md            # Project README with setup instructions and general info
│   └── setup-cfg            # Setup configuration for tooling and packaging
├── .gitignore               # Specifies intentionally untracked files to ignore
├── .sample.env              # Sample environment configuration file
└── docker-compose.yml       # Docker Compose configuration to orchestrate containers
```
