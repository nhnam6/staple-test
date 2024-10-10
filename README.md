# Staple Test

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
