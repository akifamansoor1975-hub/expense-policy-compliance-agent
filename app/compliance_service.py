from app.schemas import ExpenseClaim, ComplianceResult
from app.policy_reader import (
    extract_policy_limits,
    is_receipt_required
)


def check_compliance(expense: ExpenseClaim):

    category = expense.category.lower()

    # Get policy limits from the company policy file
    policy_limits = extract_policy_limits()

    # Check the receipt requirement from the company policy
    if is_receipt_required() and not expense.receipt_available:
        return ComplianceResult(
            status="Needs Human Review",
            explanation="The expense cannot be fully checked because the receipt is not available.",
            policy_reference="Receipt is required according to the company policy.",
            missing_information=["Receipt"],
            future_guidance="Upload the receipt and submit the expense again."
        )

    # Check if a policy exists for the expense category
    if category not in policy_limits:
        return ComplianceResult(
            status="Needs Human Review",
            explanation=f"No policy rule is available for the {expense.category} category.",
            policy_reference="No matching policy rule found.",
            missing_information=[],
            future_guidance="Send this expense for human review."
        )

    # Get the allowed limit from the policy document
    allowed_limit = policy_limits[category]

    # Check if the expense is within the allowed limit
    if expense.amount <= allowed_limit:
        return ComplianceResult(
            status="Compliant",
            explanation=f"The {category} expense of PKR {expense.amount} is within the allowed limit of PKR {allowed_limit}.",
            policy_reference=f"{category.title()} expense limit: PKR {allowed_limit}.",
            missing_information=[],
            future_guidance=f"Keep future {category} expenses within the approved limit."
        )

    # Calculate how much the expense exceeds the limit
    extra_amount = expense.amount - allowed_limit

    return ComplianceResult(
        status="Not Compliant",
        explanation=f"The {category} expense exceeds the allowed limit by PKR {extra_amount}.",
        policy_reference=f"{category.title()} expense limit: PKR {allowed_limit}.",
        missing_information=[],
        future_guidance=f"For future {category} expenses, do not exceed PKR {allowed_limit}."
    )