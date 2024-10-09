import graphene


class AgeGroupRange(graphene.ObjectType):
    min_age = graphene.Int(description="Minimum age")
    max_age = graphene.Int(description="Maximum age")


class WorkExperienceYearRange(graphene.ObjectType):
    min_years = graphene.Int(description="Minimum years of work experience")
    max_years = graphene.Int(description="Maximum years of work experience")


class CompanySizeRange(graphene.ObjectType):
    min_size = graphene.Int(description="Minimum company size")
    max_size = graphene.Int(description="Maximum company size")


class HoursPerWeekRange(graphene.ObjectType):
    min_hours = graphene.Int(description="Minimum hours per week")
    max_hours = graphene.Int(
        description="Maximum hours per week",
        default_value=168,
    )  # max hours = 7 * 24 = 168


class WorkExperienceDetails(graphene.ObjectType):
    years_in_industry = graphene.Field(
        WorkExperienceYearRange, description="Years in industry"
    )
    years_in_current_company = graphene.Field(
        WorkExperienceYearRange, description="Years in current company"
    )


class EmploymentDetails(graphene.ObjectType):
    employment_type = graphene.String()
    company_name = graphene.String()
    company_size = graphene.Field(CompanySizeRange, description="Company size")
    location_country = graphene.String()
    location_city = graphene.String()
    industry = graphene.String()
    public_private = graphene.String()


class JobDetails(graphene.ObjectType):
    title = graphene.String()
    ladder = graphene.String()
    level = graphene.Int()
    industry = graphene.String(description="Industry")
    required_hours_per_week = graphene.Field(
        HoursPerWeekRange, description="Required hours per week"
    )
    actual_hours_per_week = graphene.Field(
        HoursPerWeekRange, description="Actual hours per week"
    )
    additional_context = graphene.String(description="Additional context")


class AnnualSalary(graphene.ObjectType):
    year = graphene.Int()
    salary = graphene.Float()


class SalaryDetails(graphene.ObjectType):
    annual_salary = graphene.Float(description="Annual salary")
    currency_salary = graphene.String(description="Currency salary")
    base_salary_by_year = graphene.List(AnnualSalary)
    bonus_by_year = graphene.List(AnnualSalary)
    stock_options = graphene.Float()


class PersonalDetails(graphene.ObjectType):
    age_group = graphene.Field(AgeGroupRange, description="Age group")
    education = graphene.String()
    health_insurance = graphene.String()
    annual_vacation_weeks = graphene.Int()
    happiness = graphene.String()
    resignation_plan = graphene.String()
    industry_thoughts = graphene.String()
    gender = graphene.String()
    top_skills = graphene.String()
    bootcamp_experience = graphene.String()
    location = graphene.String(description="Location")
    work_experience = graphene.Field(
        WorkExperienceYearRange, description="Work experience"
    )


class SalarySurvey(graphene.ObjectType):
    id = graphene.String(description="Unique identifier")
    timestamp = graphene.Int(description="Epoch time in seconds")
    employment_details = graphene.Field(EmploymentDetails)
    work_experience_details = graphene.Field(WorkExperienceDetails)
    job_details = graphene.Field(JobDetails)
    salary_details = graphene.Field(SalaryDetails)
    personal_details = graphene.Field(PersonalDetails)
