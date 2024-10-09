import pandas as pd


def prepare_data_for_indexing(df: pd.DataFrame) -> list[dict]:
    # Transform the DataFrame into a list of dictionaries
    data = []
    for _, row in df.iterrows():
        entry = {
            "timestamp": row["timestamp"],
            "employment_details": {
                "employment_type": row["employment_type"],
                "company_name": row["company_name"],
                "industry": row["industry"],
                "company_size": {
                    "gte": row["company_size_min"],
                    "lte": row["company_size_max"],
                },
                "location_country": row["location_country"],
                "location_city": row["location_city"],
                "public_private": row["public_private"],
            },
            "job_details": {
                "title": row["job_title"],
                "ladder": row["ladder"],
                "level": row["level"],
                "industry": row["industry"],
                "required_hours_per_week": {
                    "gte": row["required_hours_per_week_min"],
                    "lte": row["required_hours_per_week_max"],
                },
                "actual_hours_per_week": {
                    "gte": row["actual_hours_per_week_min"],
                    "lte": row["actual_hours_per_week_max"],
                },
            },
            "salary_details": {
                "base_salary_by_year": [
                    {
                        "year": 2018,
                        "salary": row["base_salary_by_2018"],
                    }
                ],
                "bonus_by_year": [
                    {
                        "year": 2018,
                        "salary": row["bonus_by_2018"],
                    }
                ],
                "stock_options": row["stock_options"],
            },
            "personal_details": {
                "education": row["education"],
                "health_insurance": row["health_insurance"],
                "annual_vacation_weeks": row["annual_vacation_weeks"],
                "happiness": row["happy_at_current_position"],
                "registration_plan": row["resignation_plan"],
                "industry_thoughts": row["industry_thoughts"],
                "gender": row["gender"],
                "top_skills": row["top_skills"],
                "bootcamp_experience": row["bootcamp"],
            },
        }
        data.append(entry)
    return data
