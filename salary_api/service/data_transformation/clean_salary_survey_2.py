import re

import pandas as pd

from service.data_transformation.heplers import (
    GENDER_DEFAULT,
    split_range,
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

    # Standardize 'Employment Type' column
    df["employment_type"] = df["employment_type"].fillna("")

    # Standardize 'Company Name' column
    df["company_name"] = df["company_name"].fillna("")

    # Standardize 'Company Size' column
    df[["company_size_min", "company_size_max"]] = df["company_size_employees"].apply(
        lambda x: pd.Series(split_range(x))
    )

    # Standardize 'Primary Location (Country)' column
    df["location_country"] = df["primary_location_country"].fillna("")

    # Standardize 'Primary Location (City)' column
    df["location_city"] = df["primary_location_city"].fillna("")

    # Standardize 'Industry in Company' column
    df["industry"] = df["industry_in_company"].fillna("")

    # Standardize 'Public or Private Company' column
    df["public_private"] = df["public_or_private_company"].fillna("")

    # Standardize 'Years Experience in Industry' column
    df["years_experience_in_industry"] = df["years_experience_in_industry"].replace(
        "20+ years", "20-100"
    )
    df[["years_experience_in_industry_min", "years_experience_in_industry_max"]] = df[
        "years_experience_in_industry"
    ].apply(lambda x: pd.Series(split_range(x)))

    # Standardize 'Job Title In Company' column
    df["job_title"] = df["job_title_in_company"].fillna("")

    # Standardize 'Job Ladder' column
    df["ladder"] = df["job_ladder"].fillna("")

    # Standardize 'Job Level' column
    def find_job_level_num(job_level):
        # Use regex to find all numbers in the string
        numbers = re.findall(r"\d+", job_level)
        if numbers:
            return int(numbers[0])
        return 0

    df["level"] = df["job_level"].apply(lambda x: pd.Series(find_job_level_num(str(x))))

    # Standardize 'Required Hours Per Week' column
    df["required_hours_per_week"] = df["required_hours_per_week"].replace(
        "40+", "40-168"
    )
    df[["required_hours_per_week_min", "required_hours_per_week_max"]] = df[
        "required_hours_per_week"
    ].apply(lambda x: pd.Series(split_range(x)))

    # Standardize 'Actual Hours Per Week' column
    df[["actual_hours_per_week_min", "actual_hours_per_week_max"]] = df[
        "actual_hours_per_week"
    ].apply(lambda x: pd.Series(split_range(x)))

    # Standardize 'Highest Level of Formal Education Completed' column
    df["education"] = df["highest_level_of_formal_education_completed"].fillna("")

    # Standardize 'Total Base Salary in 2018 (in USD)' column
    df["base_salary_by_2018"] = df["total_base_salary_in_2018_in_usd"].fillna(0)

    # Standardize 'Total Bonus in 2018 (cumulative annual value in USD)' column
    df["bonus_by_2018"] = df[
        "total_bonus_in_2018_cumulative_annual_value_in_usd"
    ].fillna(0)

    # Standardize 'Total Stock Options/Equity in 2018 (cumulative annual value in USD)' column
    df["stock_options"] = df[
        "total_stock_options_equity_in_2018_cumulative_annual_value_in_usd"
    ].fillna(0)

    # Standardize 'Health Insurance Offered' column
    df["health_insurance"] = df["health_insurance_offered"].fillna("N/A")

    # Standardize 'Annual Vacation (in Weeks)' column
    df["annual_vacation_in_weeks"] = df["annual_vacation_in_weeks"].apply(
        lambda x: pd.Series(find_job_level_num(str(x)))
    )

    df["annual_vacation_weeks"] = df["annual_vacation_in_weeks"].fillna(0)

    # Standardize 'Are you happy at your current position?' column
    df["happy_at_current_position"] = df[
        "are_you_happy_at_your_current_position"
    ].fillna("It's Complicated")

    # Standardize 'Do you plan to resign in the next 12 months?' column
    df["resignation_plan"] = df["do_you_plan_to_resign_in_the_next_12_months"].fillna(
        "Don't know"
    )

    # Standardize 'What are your thoughts about the direction of your industry?' column
    df["industry_thoughts"] = df[
        "what_are_your_thoughts_about_the_direction_of_your_industry"
    ].fillna("")

    # Standardize 'Gender' column
    df["gender"] = df["gender"].fillna(GENDER_DEFAULT)

    # Standardize 'Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?' column
    df["top_skills"] = df[
        "final_question_what_are_the_top_skills_you_define_what_that_means_that_you_believe_will_be_necessary_for_job_growth_in_your_industry_over_the_next_10_years"
    ].fillna("")

    # Standardize 'Have you ever done a bootcamp? If so was it worth it?' column
    df["bootcamp"] = df["have_you_ever_done_a_bootcamp_if_so_was_it_worth_it"].fillna(
        ""
    )

    cleaned_df = df[
        [
            "timestamp",
            "employment_type",
            "company_name",
            "company_size_min",
            "company_size_max",
            "location_country",
            "location_city",
            "industry",
            "public_private",
            "years_experience_in_industry_min",
            "years_experience_in_industry_max",
            "job_title",
            "ladder",
            "level",
            "required_hours_per_week_min",
            "required_hours_per_week_max",
            "actual_hours_per_week_min",
            "actual_hours_per_week_max",
            "education",
            "base_salary_by_2018",
            "bonus_by_2018",
            "stock_options",
            "health_insurance",
            "annual_vacation_weeks",
            "happy_at_current_position",
            "resignation_plan",
            "industry_thoughts",
            "gender",
            "top_skills",
            "bootcamp",
        ]
    ].copy()
    cleaned_df.columns = [
        "timestamp",
        "employment_type",
        "company_name",
        "company_size_min",
        "company_size_max",
        "location_country",
        "location_city",
        "industry",
        "public_private",
        "years_experience_in_industry_min",
        "years_experience_in_industry_max",
        "job_title",
        "ladder",
        "level",
        "required_hours_per_week_min",
        "required_hours_per_week_max",
        "actual_hours_per_week_min",
        "actual_hours_per_week_max",
        "education",
        "base_salary_by_2018",
        "bonus_by_2018",
        "stock_options",
        "health_insurance",
        "annual_vacation_weeks",
        "happy_at_current_position",
        "resignation_plan",
        "industry_thoughts",
        "gender",
        "top_skills",
        "bootcamp",
    ]
    return cleaned_df
