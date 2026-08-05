from pathlib import Path
import re


def read_policy():

    policy_file = Path("data/company_policy.txt")

    with open(policy_file, "r", encoding="utf-8") as file:
        policy_text = file.read()

    return policy_text


def extract_policy_limits():

    policy_text = read_policy()

    limits = {}

    patterns = {
        "meal": r"meal expense is PKR ([\d,]+)",
        "travel": r"travel expense is PKR ([\d,]+)",
        "accommodation": r"accommodation expense is PKR ([\d,]+)"
    }

    for category, pattern in patterns.items():

        match = re.search(pattern, policy_text, re.IGNORECASE)

        if match:
            amount = match.group(1).replace(",", "")
            limits[category] = float(amount)

    return limits