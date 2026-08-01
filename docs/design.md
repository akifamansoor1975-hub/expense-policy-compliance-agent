# Design Document

## Project Title

AI-Powered Expense Policy Compliance Agent

## 1. Design Overview

The project will use FastAPI as the backend and Swagger UI for API testing.

A separate frontend or custom UI will not be created.

The core processing flow is:

```text
FastAPI → AI Agent → Policy Retrieval Tool → Pinecone → Structured Result
```

## 2. API Endpoints

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/policy/upload` | `POST` | Upload and process the company policy |
| `/compliance/check` | `POST` | Check an expense against the policy |
| `/compliance/{id}/clause` | `GET` | View the policy clause used |
| `/policy/versions` | `GET` | View available policy versions |
| `/health` | `GET` | Check whether the API is running |

## 3. Expense Request Design

The user will submit the following information through Swagger UI:

- expense category
- amount
- currency
- expense date
- business purpose
- receipt availability

Example request:

```json
{
  "expense_category": "Meal",
  "amount": 7000,
  "currency": "PKR",
  "expense_date": "2026-08-01",
  "business_purpose": "Client dinner",
  "receipt_available": true
}
```

## 4. Result Design

The API response will include:

- compliance status
- clear explanation
- policy reference
- policy limit
- submitted amount
- extra amount, if applicable
- missing information
- future guidance

Example response:

```json
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
```

## 5. System Flow

```text
User
  ↓
Swagger UI
  ↓
FastAPI
  ↓
Pydantic validation
  ↓
AI agent
  ↓
Policy retrieval tool
  ↓
Pinecone
  ↓
Relevant policy rule
  ↓
Compliance result
  ↓
Output guardrail
  ↓
JSON response
```

## 6. Design Rules

The design follows these rules:

- the API must be simple and easy to test
- input must be validated with Pydantic
- the AI agent must rely on the company policy
- every policy-based result must include a policy reference
- the final response must match the defined schema
- API keys must be stored in a `.env` file
- the system must not make the final reimbursement or payment decision

## 7. Final Design Summary

The solution will use FastAPI and Swagger UI instead of a separate frontend. A user will submit expense details through Swagger UI. The AI agent will search the company policy, compare the expense claim to the relevant rule, and return a clear, structured JSON result based on policy evidence.
