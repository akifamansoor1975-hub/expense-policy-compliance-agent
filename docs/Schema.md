Schema Document
Project Title
AI-Powered Expense Policy Compliance Agent

1. Introduction
This document explains the data structure used in the project.
The schemas will define:
What expense information the user will send
What policy information the system will use
What result the AI agent will return
What error information the API will return
These schemas will later be created using Pydantic in the FastAPI project.

2. Expense Claim Schema
This schema will store the expense information sent by the user.
Schema Name
ExpenseClaim
Fields
Field Name
Data Type
Required
Description
expense_category
String
Yes
Type of expense, such as Meal, Travel, or Accommodation
amount
Float
Yes
Total expense amount
currency
String
Yes
Currency of the expense, such as PKR or USD
expense_date
Date
Yes
Date when the expense happened
business_purpose
String
Yes
Reason for the business expense
receipt_available
Boolean
Yes
Shows whether a receipt is available

Example Input
{
  "expense_category": "Meal",
  "amount": 7000,
  "currency": "PKR",
  "expense_date": "2026-08-01",
  "business_purpose": "Client dinner",
  "receipt_available": true
}


3. Policy Metadata Schema
This schema will store important information about the company policy.
The policy metadata will help the system identify which policy rule was used.
Schema Name
PolicyMetadata
Fields
Field Name
Data Type
Required
Description
policy_version
String
Yes
Version of the company policy
effective_date
Date
Yes
Date when the policy became active
section
String
No
Policy section name or number
clause
String
No
Policy clause or rule
page_number
Integer
No
Page number where the rule is found

Example
{
  "policy_version": "1.0",
  "effective_date": "2026-01-01",
  "section": "Section 3.2",
  "clause": "Meal expenses must not exceed 5,000 PKR.",
  "page_number": 4
}


4. Policy Reference Schema
This schema will store the policy information used by the AI agent.
Schema Name
PolicyReference
Fields
Field Name
Data Type
Required
Description
section
String
No
Related policy section
clause
String
Yes
Policy rule used for the result
page_number
Integer
No
Page number of the policy rule
policy_version
String
Yes
Policy version used
effective_date
Date
Yes
Effective date of the policy

Example
{
  "section": "Section 3.2",
  "clause": "Meal expenses must not exceed 5,000 PKR.",
  "page_number": 4,
  "policy_version": "1.0",
  "effective_date": "2026-01-01"
}


5. Compliance Status Schema
The system will use the following compliance statuses:
Status
Meaning
Compliant
The expense follows the company policy
Non-Compliant
The expense breaks a company policy rule
Needs Approval
The expense needs approval or a human decision
Policy is Silent
No clear rule was found in the company policy


6. Compliance Result Schema
This schema will store the final result created by the AI agent.
Schema Name
ComplianceResult
Fields
Field Name
Data Type
Required
Description
status
String
Yes
Final compliance status
explanation
String
Yes
Clear reason for the result
policy_reference
PolicyReference
No
Policy rule used for the result
policy_limit
Float
No
Maximum amount allowed by the policy
submitted_amount
Float
Yes
Amount submitted by the user
extra_amount
Float
No
Amount above the policy limit
missing_information
List of Strings
No
Missing or unclear information
guidance
String
Yes
Policy-based advice for future expenses

Example: Non-Compliant Result
{
  "status": "Non-Compliant",
  "explanation": "The meal expense is above the allowed policy limit.",
  "policy_reference": {
    "section": "Section 3.2",
    "clause": "Meal expenses must not exceed 5,000 PKR.",
    "page_number": 4,
    "policy_version": "1.0",
    "effective_date": "2026-01-01"
  },
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "missing_information": [],
  "guidance": "For future expenses, keep the amount within 5,000 PKR or get approval if required."
}


7. Policy Silent Result
If the company policy does not contain a clear rule about the expense, the system will return:
{
  "status": "Policy is Silent",
  "explanation": "No clear rule was found in the company policy for this expense.",
  "policy_reference": null,
  "policy_limit": null,
  "submitted_amount": 7000,
  "extra_amount": null,
  "missing_information": [],
  "guidance": "Please ask a finance officer for guidance because the policy does not clearly cover this expense."
}

The system must not create or assume a policy rule.

8. Needs Approval Result
If the policy requires approval or the expense information is not enough, the system may return:
{
  "status": "Needs Approval",
  "explanation": "The expense is above the normal limit and requires manager approval.",
  "policy_reference": {
    "section": "Section 3.3",
    "clause": "Expenses above the normal limit require manager approval.",
    "page_number": 5,
    "policy_version": "1.0",
    "effective_date": "2026-01-01"
  },
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "missing_information": [],
  "guidance": "Please get manager approval before submitting this expense."
}


9. Missing Information Result
If important expense information is missing, the system may return:
{
  "status": "Needs Approval",
  "explanation": "The expense cannot be checked because the business purpose is missing.",
  "policy_reference": null,
  "policy_limit": null,
  "submitted_amount": 7000,
  "extra_amount": null,
  "missing_information": [
    "Business purpose"
  ],
  "guidance": "Please provide the business purpose and submit the expense again."
}


10. Policy Upload Response Schema
This schema will be used after a company policy is uploaded and processed.
Schema Name
PolicyUploadResponse
Fields
Field Name
Data Type
Required
Description
message
String
Yes
Success message
policy_version
String
Yes
Uploaded policy version
effective_date
Date
Yes
Policy effective date
chunks_created
Integer
Yes
Number of policy chunks created
status
String
Yes
Policy processing status

Example
{
  "message": "Policy uploaded and processed successfully.",
  "policy_version": "1.0",
  "effective_date": "2026-01-01",
  "chunks_created": 25,
  "status": "Success"
}


11. Error Response Schema
This schema will return clear error information when something goes wrong.
Schema Name
ErrorResponse
Fields
Field Name
Data Type
Required
Description
error
String
Yes
Error name
message
String
Yes
Clear explanation of the error
details
String
No
Additional error information

Example
{
  "error": "PolicyNotFound",
  "message": "The company policy is not available.",
  "details": "Please upload and process the company policy first."
}


12. Schema Relationships
The schemas will be connected in this way:
ExpenseClaim
      ↓
AI Agent
      ↓
PolicyReference
      ↓
ComplianceResult

The policy document will provide the information used in PolicyReference.
The final API response will use ComplianceResult.

13. Pydantic Model Structure
The project may use the following Pydantic models:
ExpenseClaim
PolicyMetadata
PolicyReference
ComplianceResult
PolicyUploadResponse
ErrorResponse

These models will later be created in Python.

14. Validation Rules
The system will check the following rules:
expense_category cannot be empty
amount must be greater than zero
currency cannot be empty
expense_date must be a valid date
business_purpose cannot be empty
receipt_available must be true or false
page_number must be greater than zero
policy_version cannot be empty
status must be a valid compliance status

15. Final Schema Summary
The main schemas are:
ExpenseClaim — Stores expense information from the user
PolicyMetadata — Stores company policy information
PolicyReference — Stores the policy rule used by the AI agent
ComplianceResult — Stores the final compliance result
PolicyUploadResponse — Returns the policy upload result
ErrorResponse — Returns error information
These schemas will keep the API input and output clear, organized, and consistent.
