import pandas as pd


def prepare_data_for_indexing(df: pd.DataFrame) -> list[dict]:
    # Transform the DataFrame into a list of dictionaries
    data = []
    for _, row in df.iterrows():
        entry = {
            "timestamp": row["timestamp"],
            "job_details": {
                "title": row["job_title"],
                "additional_context": row["additional_context"],
            },
            "personal_details": {
                "gender": row["gender"],
                "work_experience": {
                    "gte": row["years_experience_min"],
                    "lte": row["years_experience_max"],
                },
                "location": row["location"],
            },
        }
        data.append(entry)
    return data
