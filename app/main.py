from fastapi import FastAPI

from app.schemas import ExpenseClaim, ComplianceResult
from app.policy_reader import read_policy, extract_policy_limits


app = FastAPI(
    title="Expense Policy Compliance Agent",
    description="An AI-powered API for checking employee expenses against company policies.",
    version="1.0.0"
)


# Get policy limits automatically from the company policy file
POLICY_LIMITS = extract_policy_limits()


@app.get("/")
def read_root():
    return {
        "message": "Expense Policy Compliance Agent API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# Read and show the company policy document
@app.get("/policy")
def get_policy():
    return {
        "policy": read_policy()
    }


@app.post("/expenses/check", response_model=ComplianceResult)
def check_expense(expense: ExpenseClaim):

    category = expense.category.lower()

    # Check if the receipt is available
    if not expense.receipt_available:
        return ComplianceResult(
            status="Needs Human Review",
            explanation="The expense cannot be fully checked because the receipt is not available.",
            policy_reference="Receipt is required for expense verification.",
            missing_information=["Receipt"],
            future_guidance="Upload the receipt and submit the expense again."
        )

    # Check if a policy exists for the category
    if category not in POLICY_LIMITS:
        return ComplianceResult(
            status="Needs Human Review",
            explanation=f"No policy rule is available for the {expense.category} category.",
            policy_reference="No matching policy rule found.",
            missing_information=[],
            future_guidance="Send this expense for human review."
        )

    # Get the allowed limit from the policy document
    allowed_limit = POLICY_LIMITS[category]

    # Check if the expense is within the limit
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