Design Document
Project Title
AI-Powered Expense Policy Compliance Agent
1. Design Overview
The project will use FastAPI as the backend and Swagger UI for testing the APIs.
A separate frontend or custom UI will not be created.
The system will use:
FastAPI → AI Agent → Policy Retrieval Tool → Pinecone → Structured Result

2. API Endpoints
Endpoint
Method
Purpose
/policy/upload
POST
Upload and process the company policy
/compliance/check
POST
Check an expense against the policy
/compliance/{id}/clause
GET
View the policy clause used
/policy/versions
GET
View available policy versions
/health
GET
Check whether the API is running


3. Expense Request Design
The user will enter these details in Swagger UI:
Expense category
Amount
Currency
Expense date
Business purpose
Receipt availability
Example:
{
  "expense_category": "Meal",
  "amount": 7000,
  "currency": "PKR",
  "expense_date": "2026-08-01",
  "business_purpose": "Client dinner",
  "receipt_available": true
}


4. Result Design
The API response will include:
Compliance status
Clear explanation
Policy reference
Policy limit
Submitted amount
Extra amount, if applicable
Missing information
Future guidance
Example:
{
  "status": "Non-Compliant",
  "explanation": "The expense is above the allowed policy limit.",
  "policy_reference": "Section 3.2",
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "missing_information": [],
  "guidance": "Keep future expenses within the policy limit."
}


5. System Flow
User
↓
Swagger UI
↓
FastAPI
↓
Pydantic Validation
↓
AI Agent
↓
Policy Retrieval Tool
↓
Pinecone
↓
Relevant Policy Rule
↓
Compliance Result
↓
Output Guardrail
↓
JSON Response


6. Design Rules
The API must be simple and easy to test.
Input must be validated using Pydantic.
The AI agent must use the company policy.
Every policy-based result must include a policy reference.
The final response must follow the defined schema.
API keys must be stored in a .env file.
The system will not make the final payment or reimbursement decision.

7. Final Design Summary
The project will use FastAPI and Swagger UI instead of a separate frontend.
The user will submit expense details through Swagger UI. The AI agent will search the company policy, check the expense, and return a clear, policy-based JSON result.

