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
staple_test-es-1                     docker.elastic.co/elasticsearch/elasticsearch:8.7.1   "/bin/tini -- /usr/l…"   es                     2 days ago           Up 4 hours          0.0.0.0:9200->9200/tcp, 9300/tcp
staple_test-kibana-1                 docker.elastic.co/kibana/kibana:8.7.1                 "/bin/tini -- /usr/l…"   kibana                 2 days ago           Up 4 hours          0.0.0.0:5601->5601/tcp
staple_test-salary_survey_server-1   staple_test-salary_survey_server                      "pipenv run runserver"   salary_survey_server   About a minute ago   Up About a minute   0.0.0.0:5001->5000/tcp
```

4. Viewing output

```
docker compose logs -f --tail 100 salary_survey_server
```

Example log:

```
alary_survey_server-1  |  * Serving Flask app 'main.py'
salary_survey_server-1  |  * Debug mode: on
salary_survey_server-1  | 2024-10-09 19:13:14,806 - INFO - werkzeug - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
salary_survey_server-1  |  * Running on all addresses (0.0.0.0)
salary_survey_server-1  |  * Running on http://127.0.0.1:5000
salary_survey_server-1  |  * Running on http://172.22.0.4:5000
salary_survey_server-1  | 2024-10-09 19:13:14,806 - INFO - werkzeug - Press CTRL+C to quit
salary_survey_server-1  | 2024-10-09 19:13:14,807 - INFO - werkzeug -  * Restarting with stat
salary_survey_server-1  | 2024-10-09 19:13:16,406 - WARNING - werkzeug -  * Debugger is active!
salary_survey_server-1  | 2024-10-09 19:13:16,409 - INFO - werkzeug -  * Debugger PIN: 732-871-805`
```

## Exercise

1. Exercise A: https://github.com/nhnam6/staple-test/blob/main/docs/Exercise-A/README.md

2. Exercise B: https://github.com/nhnam6/staple-test/blob/main/docs/Exercise-B/README.md
