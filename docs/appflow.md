# Application Flow Document

## Project Title

AI-Powered Expense Policy Compliance Agent

## 1. Overview

This document explains the end-to-end application flow for the AI-Powered Expense Policy Compliance Agent.

The system has two main flows:

- Policy processing flow
- Expense checking flow

The application will use FastAPI as the backend and Swagger UI for API testing and demonstration.

## 2. Policy Processing Flow

This flow is used when a company policy document is added to the system.

### Step 1: Company provides the policy

The company provides an expense policy document containing rules for areas such as:

- meals
- travel
- accommodation
- transportation
- office supplies
- receipts
- expense limits
- approval requirements

### Step 2: Policy document is loaded

The system reads the policy document using LangChain.

### Step 3: Policy text is split into chunks

The policy may be long, so it is divided into smaller text chunks. Each chunk can include:

- policy rule
- section number
- clause text
- page number
- policy version
- effective date

### Step 4: Embeddings are created

Each text chunk is converted into a vector embedding. These embeddings help the system find policy information related to an expense claim.

### Step 5: Policy information is stored

The embeddings and associated metadata are stored in Pinecone, which becomes the searchable policy knowledge base.

### Policy processing flow diagram

```text
Company Expense Policy PDF
  ↓
LangChain loads the PDF
  ↓
Policy text is extracted
  ↓
Text is split into chunks
  ↓
Embeddings are created
  ↓
Chunks and metadata are stored in Pinecone
  ↓
Policy is ready for search
```

## 3. Expense Checking Flow

This flow is used when a user submits an expense for compliance checking.

### Step 1: User opens Swagger UI

The user opens the FastAPI Swagger UI and selects the expense compliance API.

### Step 2: User enters expense details

The user submits fields such as:

- expense category
- expense amount
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

### Step 3: User sends the request

The user clicks Execute in Swagger UI. The request is sent to the FastAPI backend.

### Step 4: FastAPI validates the input

FastAPI validates the request and checks whether:

- the expense category is present
- the amount is valid
- the date is valid
- the business purpose is present
- receipt information is available

If the input is invalid, FastAPI returns an error. If valid, the request moves to the AI agent.

### Step 5: AI agent reads the expense

The AI agent reads the request and identifies the relevant dimensions needed for checking.

### Step 6: AI agent searches the policy

The AI agent uses the policy retrieval function tool to search Pinecone for relevant rules.

### Step 7: Pinecone returns policy information

Pinecone returns the most relevant policy chunks, including metadata such as:

- policy rule
- policy section
- clause
- page number
- policy version
- effective date

### Step 8: AI agent checks the expense against policy

The AI agent compares the expense details with the retrieved rule and checks whether:

- the expense is compliant
- the amount exceeds the limit
- approval is required
- required information is missing
- the policy is clear for this case

### Step 9: AI agent creates the result

The AI agent returns a structured result containing:

- compliance status
- explanation
- policy reference
- policy limit
- submitted amount
- extra amount
- missing information
- guidance

### Step 10: Output guardrail validates the response

The output guardrail checks that the result:

- includes a policy reference when needed
- is based on retrieved policy evidence
- follows the expected schema
- does not invent or assume policy content

### Step 11: FastAPI returns the final JSON response

FastAPI returns the result to Swagger UI in JSON format.

Example response:

```json
{
  "status": "Non-Compliant",
  "explanation": "The meal expense is above the allowed policy limit.",
  "policy_reference": "Section 3.2 — Meal Expenses",
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "guidance": "For future expenses, keep the amount within 5,000 PKR or get approval if required."
}
```

## 4. End-to-End Flow Summary

```text
User
  ↓
Swagger UI
  ↓
Expense details are entered
  ↓
FastAPI receives the request
  ↓
Pydantic validates the input
  ↓
AI agent reads the request
  ↓
Policy retrieval tool searches Pinecone
  ↓
Relevant policy rule is returned
  ↓
AI agent compares expense with policy
  ↓
Structured result is created
  ↓
Output guardrail validates result
  ↓
FastAPI returns JSON response
  ↓
Result is displayed in Swagger UI
```

## 5. Decision Flow

The AI agent follows a simple decision process:

1. Is the expense information complete?
   - If no, identify missing information and return `Needs Approval`.
   - If yes, continue.
1. Search the company policy.
1. Retrieve the most relevant policy rule.
1. Compare the expense with the policy.
1. Return a policy-based compliance result.

## 6. Final Notes

The system is designed to support policy-based decision assistance rather than final payment authorization. The responsible finance officer or authorized employee remains the final decision-maker.
↓
Was a Relevant Policy Rule Found?
│
├── No
│ ↓
│ Return:
│ "Policy is silent on this."
│
└── Yes
↓
Compare Expense with Policy
↓
Does the Expense Follow the Policy?
│
├── Yes
│ ↓
│ Return Compliant
│
└── No
↓
Is Approval Allowed by the Policy?
│
├── Yes
│ ↓
│ Return Needs Approval
│
└── No
↓
Return Non-Compliant

1. Main Result Types
   6.1 Compliant
   The expense follows the company policy.
   Example:
   The meal expense is 4,500 PKR. The policy allows meal expenses up to 5,000 PKR. Therefore, the expense is compliant.

6.2 Non-Compliant
The expense breaks a company policy rule.
Example:
The meal expense is 7,000 PKR. The policy limit is 5,000 PKR. The expense is 2,000 PKR above the allowed limit. Therefore, the expense is non-compliant.

6.3 Needs Approval
The expense may require approval or human review.
Example:
The expense is above the normal limit, but the company policy allows higher expenses with manager approval.

6.4 Policy Is Silent
The company policy does not contain a clear rule about the expense.
Example:
No clear policy rule was found for this type of expense. The policy is silent on this matter.
The system will not create or assume a policy rule.

7. Error Flow
   The system will handle the following errors:
   Invalid Expense Information
   If the user enters invalid information, FastAPI will return a validation error.
   Examples:
   Expense amount is missing
   Expense amount is negative
   Expense date is invalid
   Expense category is missing

Policy Is Not Available
If the company policy has not been processed, the system will return:
“The company policy is not available. Please upload and process the policy first.”

Policy Search Error
If Pinecone cannot return policy information, the system will return a clear error message.

AI Agent Error
If the AI agent cannot complete the request, the system will return an error message.

Missing Policy Reference
If the AI result does not contain a policy reference, the output guardrail will stop the result.

8. Final Application Flow Summary
   The complete application flow is:
   Company Policy PDF
   ↓
   Load Policy
   ↓
   Split Policy into Chunks
   ↓
   Create Embeddings
   ↓
   Store in Pinecone
   ↓
   Policy Is Ready

User Expense Details
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
Pinecone Search
↓
Relevant Policy Rule
↓
Policy-Based Expense Check
↓
Structured Result
↓
Output Guardrail
↓
JSON Response
↓
Swagger UI

The system will use the company policy as the main source of information and will provide a clear, explainable, and policy-based expense result.
