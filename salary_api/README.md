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
