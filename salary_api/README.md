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

### Run Flask app

```
flask --app main --debug run
```

### Run custom commands

1. Load salary survey data (salary_survey-1.csv)

```
flask load-salary survey-1 data/salary_survey-1.csv
```

2. Load salary survey data (salary_survey-2.cs)

```
flask load-salary survey-2 data/salary_survey-2.csv
```

3. Load salary survey data (salary_survey-3.csv)

```
flask load-salary survey-3 data/salary_survey-3.csv
```
