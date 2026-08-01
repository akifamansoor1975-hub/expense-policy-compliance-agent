Application Flow Document
Project Title
AI-Powered Expense Policy Compliance Agent

1. Introduction
This document explains how the AI-Powered Expense Policy Compliance Agent works from start to end.
The application has two main flows:
Policy Processing Flow — The company expense policy is prepared and stored in Pinecone.
Expense Checking Flow — The user submits an expense, and the AI agent checks it using the company policy.
The project will use FastAPI APIs. The APIs will be tested and demonstrated using Swagger UI.

2. Policy Processing Flow
This flow happens when the company expense policy is added to the system.
Step 1: Company Provides the Policy
The company provides an expense policy document.
The policy may contain rules about:
Meals
Travel
Accommodation
Transportation
Office supplies
Receipts
Expense limits
Approval requirements

Step 2: Policy Document Is Loaded
The system reads the company expense policy document.
LangChain will be used to load and read the policy document.

Step 3: Policy Text Is Split
The policy document may be long.
The system will divide the policy text into smaller parts called chunks.
Each chunk may contain information such as:
Policy rule
Policy section
Policy clause
Page number
Policy version
Effective date

Step 4: Embeddings Are Created
The system will convert each policy chunk into a vector.
These vectors are called embeddings.
Embeddings help the system find policy information that is related to an expense.

Step 5: Policy Information Is Stored
The policy embeddings and related information will be stored in Pinecone.
Pinecone will become the searchable policy knowledge base.

Policy Processing Flow Diagram
Company Expense Policy PDF
            ↓
LangChain Loads the PDF
            ↓
Policy Text Is Extracted
            ↓
Text Is Split into Chunks
            ↓
Embeddings Are Created
            ↓
Chunks and Metadata Are Stored in Pinecone
            ↓
Policy Is Ready for Search


3. Expense Checking Flow
This flow happens when a user wants to check an expense.
Step 1: User Opens Swagger UI
The user opens the FastAPI Swagger UI.
The user selects the expense compliance API.

Step 2: User Enters Expense Details
The user enters expense information.
The information may include:
Expense category
Expense amount
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


Step 3: User Sends the Request
The user clicks the Execute button in Swagger UI.
The expense information is sent to the FastAPI backend.

Step 4: FastAPI Validates the Input
FastAPI checks the submitted information.
The system checks:
Is the expense category provided?
Is the expense amount valid?
Is the expense date valid?
Is the business purpose provided?
Is the receipt information provided?
If the input is invalid, FastAPI returns an error message.
If the input is valid, the request is sent to the AI agent.

Step 5: AI Agent Understands the Expense
The AI agent reads the expense information.
The agent identifies:
Expense category
Expense amount
Expense date
Business purpose
Important details that may be needed for policy checking

Step 6: AI Agent Searches the Policy
The AI agent uses the Policy Retrieval Function Tool.
The tool searches Pinecone for the policy rules related to the expense.
For example:
User expense: Client dinner — 7,000 PKR
The tool may search for:
Meal expense limits, client dinner rules, and approval requirements

Step 7: Pinecone Returns Relevant Policy Information
Pinecone returns the most relevant policy chunks.
The returned information may include:
Policy rule
Policy section
Policy clause
Page number
Policy version
Effective date

Step 8: AI Agent Checks the Expense
The AI agent compares the submitted expense with the retrieved policy rule.
The agent checks:
Does the expense follow the policy?
Is the expense above the allowed limit?
Is approval required?
Is important information missing?
Is the policy clear about this expense?

Step 9: AI Agent Creates the Result
The AI agent creates a structured result.
The result may contain:
Compliance status
Explanation
Policy reference
Policy limit
Submitted amount
Extra amount
Missing information
Future guidance

Step 10: Output Guardrail Checks the Result
The output guardrail checks the AI result before it is returned.
The guardrail checks:
Is a policy reference included?
Is the result based on the retrieved policy?
Is the policy clause missing?
If the result does not contain the required policy reference, the system will reject or stop the result.

Step 11: FastAPI Returns the Final Response
FastAPI returns the final result in JSON format.
The result is displayed in Swagger UI.
Example:
{
  "status": "Non-Compliant",
  "explanation": "The meal expense is above the allowed policy limit.",
  "policy_reference": "Section 3.2 — Meal Expenses",
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "guidance": "For future expenses, keep the amount within 5,000 PKR or get approval if required."
}


4. Complete Expense Checking Flow
User
  ↓
Swagger UI
  ↓
Enter Expense Details
  ↓
Click Execute
  ↓
FastAPI Receives the Request
  ↓
Pydantic Validates the Input
  ↓
AI Agent Reads the Expense
  ↓
Policy Retrieval Function Tool
  ↓
Pinecone Searches the Company Policy
  ↓
Relevant Policy Rule Is Returned
  ↓
AI Agent Compares Expense with Policy
  ↓
Structured Result Is Created
  ↓
Output Guardrail Checks the Result
  ↓
FastAPI Returns JSON Response
  ↓
Result Is Displayed in Swagger UI


5. Decision Flow
The AI agent will follow this decision process:
Start
  ↓
Is the expense information complete?
  │
  ├── No
  │     ↓
  │   Identify Missing Information
  │     ↓
  │   Return Needs Approval
  │
  └── Yes
        ↓
Search the Company Policy
        ↓
Was a Relevant Policy Rule Found?
        │
        ├── No
        │     ↓
        │   Return:
        │   "Policy is silent on this."
        │
        └── Yes
              ↓
Compare Expense with Policy
              ↓
Does the Expense Follow the Policy?
              │
              ├── Yes
              │     ↓
              │   Return Compliant
              │
              └── No
                    ↓
              Is Approval Allowed by the Policy?
                    │
                    ├── Yes
                    │     ↓
                    │   Return Needs Approval
                    │
                    └── No
                          ↓
                    Return Non-Compliant


6. Main Result Types
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
