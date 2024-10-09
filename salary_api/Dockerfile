FROM python:3.11.4-slim AS base

WORKDIR /code

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV PIPENV_VENV_IN_PROJECT=1

# Install base dependencies
RUN apt-get update && apt-get install -y -q --no-install-recommends \
    apt-transport-https \
    binutils \
    build-essential \
    ca-certificates \
    curl \
    gdal-bin \
    git \
    libproj-dev \
    libssl-dev \
    libpq-dev \
    libcurl4-openssl-dev \
    wget \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/* \
    llibheif-dev

# Install & use pipenv
RUN python -m pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv sync

# Worker healthcheck
RUN touch /tmp/healthy

COPY . /code

# Make port 5000 available to the world outside this container
EXPOSE 5000
