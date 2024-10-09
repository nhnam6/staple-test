import re

import pandas as pd

from service.data_transformation.heplers import (
    parse_salary,
    split_range,
    split_work_experience,
)


def clean_and_transform_survey(df: pd.DataFrame) -> pd.DataFrame:
    # Standardize column names
    df.columns = (
        df.columns.str.lower()  # Convert to lower case
        .str.replace(
            r"[^a-z0-9]+", "_", regex=True
        )  # Replace groups of non-alphanumeric characters with '_'
        .str.strip("_")  # Remove leading/trailing underscores if any
    )
    # Drop rows with missing 'Timestamp'
    df.dropna(subset=["timestamp"], inplace=True)

    # Convert 'Timestamp' to a proper epoch time (seconds since epoch)
    df["timestamp"] = pd.to_datetime(df["timestamp"]).apply(
        lambda x: int(x.timestamp())
    )

    # Standardize 'How old are you?' column
    df["how_old_are_you"] = df["how_old_are_you"].str.replace("65 or over", "65-100")
    df["how_old_are_you"] = df["how_old_are_you"].str.replace("under 18", "0-17")

    # Split 'How old are you?' into min_age and max_age
    df[["min_age", "max_age"]] = df["how_old_are_you"].apply(
        lambda x: pd.Series(split_range(x))
    )

    # Map 'What industry do you work in??' to 'industry'
    df["industry"] = df["what_industry_do_you_work_in"]
    df["industry"] = df["industry"].fillna("")

    # Map 'What is your annual salary?' to 'annual_salary'
    df["annual_salary"] = df["what_is_your_annual_salary"].apply(parse_salary)
    df["annual_salary"] = df["annual_salary"].fillna(0)

    # Map 'Please indicate the currency' to 'currency'
    df["currency"] = df["please_indicate_the_currency"]
    df["currency"] = df["currency"].fillna("")

    # Map 'Where are you located? (City/state/country)' to 'location'
    df["location"] = df["where_are_you_located_city_state_country"]
    df["location"] = df["location"].fillna("")

    df[["min_years", "max_years"]] = df[
        "how_many_years_of_post_college_professional_work_experience_do_you_have"
    ].apply(lambda x: pd.Series(split_work_experience(x)))

    # Map 'If your job title needs additional context, please clarify here:' to 'additional_context'
    df["additional_context"] = df[
        "if_your_job_title_needs_additional_context_please_clarify_here"
    ]
    df["additional_context"] = df["additional_context"].fillna("")

    # Map 'Job title' to 'job_title'
    df["job_title"] = df["job_title"].fillna("")

    cleaned_df = df[
        [
            "timestamp",
            "min_age",
            "max_age",
            "industry",
            "job_title",
            "annual_salary",
            "currency",
            "location",
            "min_years",
            "max_years",
            "additional_context",
        ]
    ].copy()
    cleaned_df.columns = [
        "timestamp",
        "min_age",
        "max_age",
        "industry",
        "job_title",
        "annual_salary",
        "currency",
        "location",
        "min_years",
        "max_years",
        "additional_context",
    ]

    return cleaned_df
