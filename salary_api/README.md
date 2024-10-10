# Salary API Server

## Install (Mac OS)

```bash
#
# Install pyenv
# (https://github.com/pyenv/pyenv)
pyenv install $(cat .python-version)
pyenv rehash


# It is useful to register python3 alias
echo 'alias python=python3' >> ~/.zshrc
source ~/.zshrc

# Install pipenv
pip install pipenv

# Specify that the virtual environment should be created in backend/venv
echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.zshrc
source ~/.zshrc
```

## How to use

```bash
#
# Create .env file
cp .sample.env .env

# Active venv
pipenv shell

# Install development packages
pipenv run setup_dev
```

## Salary API commands

### Prerequisites

Before running the Salary API, you need to ensure that Elasticsearch and Kibana services are up and running.

1. Navigate to the Project Root Directory

```
cd path/to/staple-test
```

2. Start the Services

```
docker compose up -d es kibana
```

3. Access Kibana

```
http://localhost:5601
```

### Create index

```
pipenv run flask elasticsearch create-index
```

Example output:

```
2024-10-10 02:48:18,372 - INFO - root - Creating Elasticsearch index...
2024-10-10 02:48:18,374 - DEBUG - urllib3.connectionpool - Starting new HTTP connection (1): localhost:9200
2024-10-10 02:48:18,589 - DEBUG - urllib3.connectionpool - http://localhost:9200 "PUT /_template/salary-survey-template-202410 HTTP/11" 200 0
2024-10-10 02:48:18,589 - INFO - elastic_transport.transport - PUT http://localhost:9200/_template/salary-survey-template-202410 [status:200 duration:0.216s]
/Users/0x442/workspace/labs/staple-test/salary_api/service/search/index.py:90: ElasticsearchWarning: Legacy index templates are deprecated in favor of composable templates.
  es.indices.put_template(
2024-10-10 02:48:18,804 - INFO - root - Template salary-survey-template-202410 created/updated
2024-10-10 02:48:18,807 - DEBUG - urllib3.connectionpool - http://localhost:9200 "HEAD /salary-survey-index-202410 HTTP/11" 404 0
2024-10-10 02:48:18,808 - INFO - elastic_transport.transport - HEAD http://localhost:9200/salary-survey-index-202410 [status:404 duration:0.003s]
2024-10-10 02:48:19,215 - DEBUG - urllib3.connectionpool - http://localhost:9200 "PUT /salary-survey-index-202410 HTTP/11" 200 0
2024-10-10 02:48:19,215 - INFO - elastic_transport.transport - PUT http://localhost:9200/salary-survey-index-202410 [status:200 duration:0.407s]
2024-10-10 02:48:19,215 - INFO - root - Index salary-survey-index-202410 created
```

### Run Flask app

```
pipenv run flask --app main --debug run
```

Example output

```

 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
 * Serving Flask app 'main'
 * Debug mode: on
2024-10-10 02:48:56,740 - INFO - werkzeug - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
2024-10-10 02:48:56,740 - INFO - werkzeug - Press CTRL+C to quit
2024-10-10 02:48:56,742 - INFO - werkzeug -  * Restarting with stat
 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
2024-10-10 02:48:57,877 - WARNING - werkzeug -  * Debugger is active!
2024-10-10 02:48:57,905 - INFO - werkzeug -  * Debugger PIN: 268-871-564
```

### Run custom commands

1. Load salary survey data (salary_survey-1.csv)

```
pipenv run flask load-salary survey-1 data/salary_survey-1.csv
```

2. Load salary survey data (salary_survey-2.cs)

```
pipenv run flask load-salary survey-2 data/salary_survey-2.csv
```

3. Load salary survey data (salary_survey-3.csv)

```
pipenv run flask load-salary survey-3 data/salary_survey-3.csv
```

## Unittest

### Setup development environment

```
pipenv run setup_dev
```

2. Active the virtual environment

```
pipenv shell
```

3. Running Tests with pytest

```bash
pytest -v
```

Example output:

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
pytest --cov=./
```

Example output:

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
