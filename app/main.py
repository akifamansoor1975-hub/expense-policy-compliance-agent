from fastapi import FastAPI

from app.schemas import ExpenseClaim, ComplianceResult
from app.policy_reader import read_policy
from app.compliance_service import check_compliance


app = FastAPI(
    title="Expense Policy Compliance Agent",
    description="An AI-powered API for checking employee expenses against company policies.",
    version="1.0.0"
)


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


# Check the expense using the compliance service
@app.post("/expenses/check", response_model=ComplianceResult)
def check_expense(expense: ExpenseClaim):

    return check_compliance(expense)