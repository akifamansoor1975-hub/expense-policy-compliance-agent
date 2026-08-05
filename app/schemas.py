from datetime import date
from pydantic import BaseModel, Field

from typing import List

class ExpenseClaim(BaseModel):
    category: str = Field(
        ...,
        description="Category of the expense, such as meal, travel, or accommodation"
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount. It must be greater than zero"
    )

    currency: str = Field(
        default="PKR",
        min_length=3,
        max_length=3,
        description="Three-letter currency code"
    )

    expense_date: date

    business_purpose: str = Field(
        ...,
        min_length=5,
        description="Reason for the business expense"
    )

    receipt_available: bool
##---------------
         ###-------------------------

class ComplianceResult(BaseModel):
    status: str
    explanation: str
    policy_reference: str
    missing_information: List[str] = []
    future_guidance: str