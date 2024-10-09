import re

GENDER_DEFAULT = ""


def parse_salary(salary_str) -> float:
    try:
        # Remove commas for thousands
        salary_str = str(salary_str).replace(",", "")

        # Check for the 'k' notation and convert to float
        if "k" in salary_str.lower():
            # Remove the 'k' and convert to float, multiply by 1000
            return float(salary_str.lower().replace("k", "")) * 1000
        elif "m" in salary_str.lower():
            # Similarly handle 'm' for millions
            return float(salary_str.lower().replace("m", "")) * 1000000
        else:
            # Convert directly to float
            return float(salary_str)
    except ValueError:
        # Log or handle cases where conversion is not possible
        return float(0)


def split_range(range_str):
    try:
        min_age, max_age = map(int, range_str.split("-"))
        return min_age, max_age
    except ValueError:
        return 0, 0


def split_work_experience(exp_str):
    # Use regex to find all numbers in the string
    numbers = re.findall(r"\d+", exp_str)

    # Check how many numbers were found and process accordingly
    if len(numbers) == 2:
        # If two numbers are found, likely a range was specified
        numbers = list(map(int, numbers))
        return min(numbers), max(numbers)

    elif "Less than 1 year" in exp_str:
        return 0, 1
    elif "More than 50 years" in exp_str:
        return 50, 100
    elif len(numbers) == 1 and "+" in exp_str:
        return int(numbers[0]), 100
    elif len(numbers) == 1:
        return int(numbers[0]), int(numbers[0])
    return 0, 0
