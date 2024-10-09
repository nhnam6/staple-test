from elasticsearch import Elasticsearch

from logger.logger import logger


def create_template(es: Elasticsearch, template_name: str, indexes: list[str]):
    # Define the template with mappings and settings
    template_body = {
        "index_patterns": indexes,
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        },
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "employment_details": {
                    "properties": {
                        "employment_type": {"type": "keyword"},
                        "company_name": {"type": "text"},
                        "company_size": {"type": "integer_range"},
                        "location_country": {"type": "keyword"},
                        "location_city": {"type": "text"},
                        "industry": {"type": "text"},
                        "public_private": {"type": "text"},
                    }
                },
                "work_experience_details": {
                    "properties": {
                        "years_in_industry": {"type": "integer_range"},
                        "years_in_current_company": {"type": "integer_range"},
                    }
                },
                "job_details": {
                    "properties": {
                        "title": {"type": "text"},
                        "ladder": {"type": "text"},
                        "level": {"type": "integer"},
                        "industry": {"type": "keyword"},
                        "required_hours_per_week": {"type": "integer_range"},
                        "actual_hours_per_week": {"type": "integer_range"},
                        "additional_context": {"type": "text"},
                    }
                },
                "salary_details": {
                    "properties": {
                        "annual_salary": {"type": "float"},
                        "currency_salary": {"type": "keyword"},
                        "base_salary_by_year": {
                            "type": "nested",
                            "properties": {
                                "year": {"type": "integer"},
                                "salary": {"type": "float"},
                            },
                        },
                        "bonus_by_year": {
                            "type": "nested",
                            "properties": {
                                "year": {"type": "integer"},
                                "salary": {"type": "float"},
                            },
                        },
                        "stock_options": {"type": "float"},
                    }
                },
                "personal_details": {
                    "properties": {
                        "age_group": {"type": "integer_range"},
                        "education": {"type": "text"},
                        "health_insurance": {"type": "keyword"},
                        "annual_vacation_weeks": {"type": "integer"},
                        "happiness": {"type": "text"},
                        "resignation_plan": {"type": "text"},
                        "industry_thoughts": {"type": "text"},
                        "gender": {"type": "keyword"},
                        "top_skills": {"type": "text"},
                        "bootcamp_experience": {"type": "text"},
                        "location": {
                            "type": "text",
                            "fields": {"keyword": {"type": "keyword"}},
                        },
                        "work_experience": {"type": "integer_range"},
                    }
                },
            }
        },
    }

    # Create or update the template in Elasticsearch
    es.indices.put_template(
        name=template_name,
        body=template_body,
    )
    logger.info("Template %s created/updated", template_name)


def create_index(es: Elasticsearch, index_name: str):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        logger.info("Index %s created", index_name)
    else:
        logger.info("Index %s already exists", index_name)
