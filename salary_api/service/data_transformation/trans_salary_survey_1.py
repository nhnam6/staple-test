import pandas as pd


def prepare_data_for_indexing(df: pd.DataFrame) -> list[dict]:
    # Transform the DataFrame into a list of dictionaries
    data = []
    for _, row in df.iterrows():
        entry = {
            "timestamp": row["timestamp"],
            "employment_details": {
                "industry": row["industry"],
            },
            "job_details": {
                "title": row["job_title"],
                "industry": row["industry"],
                "additional_context": row["additional_context"],
            },
            "salary_details": {
                "annual_salary": row["annual_salary"],
                "currency_salary": row["currency"],
                "base_salary_by_year": [],
                "bonus_by_year": [],
            },
            "personal_details": {
                "age_group": {
                    "gte": row["min_age"],
                    "lte": row["max_age"],
                },
                "location": row["location"],
                "work_experience": {
                    "gte": row["min_years"],
                    "lte": row["max_years"],
                },
            },
        }
        data.append(entry)
    return data
