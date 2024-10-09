import pandas as pd

from service.data_transformation.heplers import (
    GENDER_DEFAULT,
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
    # Drop rows with missing 'Timestamp', 'Employer' and 'Job Title'
    df.dropna(subset=["timestamp", "employer", "job_title"], inplace=True)

    # Convert 'Timestamp' to a proper epoch time (seconds since epoch)
    df["timestamp"] = pd.to_datetime(df["timestamp"]).apply(
        lambda x: int(x.timestamp())
    )

    # Standardize 'Employer' column
    df["employer"] = df["employer"].fillna("")

    # Standardize 'Location' column
    df["location"] = df["location"].fillna("")

    # Standardize 'Job Title' column
    df["job_title"] = df["job_title"].fillna("")

    # Standardize 'Years at Employer' column
    def split_years_at_employer(years_str):
        if "<1" in years_str:
            return 0
        try:
            return int(years_str)
        except ValueError:
            return 0

    df["years_at_employer"] = df["years_at_employer"].apply(
        lambda x: pd.Series(split_years_at_employer(str(x)))
    )

    # Standardize 'Years of Experience' column
    df[["years_experience_min", "years_experience_max"]] = df[
        "years_of_experience"
    ].apply(lambda x: pd.Series(split_work_experience(str(x))))

    # Standardize 'Annual Base Pay' column
    df["annual_salary"] = df["annual_base_pay"].fillna(0)

    # Standardize 'Signing Bonus' column
    df["signing_bonus"] = df["signing_bonus"].fillna(0)

    # Standardize 'Annual Bonus' column
    df["annual_bonus"] = df["annual_bonus"].fillna(0)

    # Standardize 'Annual Stock Value/Bonus' column
    df["annual_stock_value_bonus"] = df["annual_stock_value_bonus"].fillna(0)

    # Standardize 'Gender' column
    df["gender"] = df["gender"].fillna(GENDER_DEFAULT)

    # Standardize 'Additional Comments' column
    df["additional_context"] = df["additional_comments"].fillna("")

    cleaned_df = df[
        [
            "timestamp",
            "employer",
            "location",
            "job_title",
            "years_at_employer",
            "years_experience_min",
            "years_experience_max",
            "annual_salary",
            "signing_bonus",
            "annual_bonus",
            "annual_stock_value_bonus",
            "gender",
            "additional_context",
        ]
    ].copy()
    cleaned_df.columns = [
        "timestamp",
        "employer",
        "location",
        "job_title",
        "years_at_employer",
        "years_experience_min",
        "years_experience_max",
        "annual_salary",
        "signing_bonus",
        "annual_bonus",
        "annual_stock_value_bonus",
        "gender",
        "additional_context",
    ]
    return cleaned_df
