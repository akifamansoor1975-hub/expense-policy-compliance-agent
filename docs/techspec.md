# Technical Specification Document

## Project Title

AI-Powered Expense Policy Compliance Agent

## 1. Introduction

This document explains how the AI-Powered Expense Policy Compliance Agent will be built.

The system uses a company expense policy document as its main source of information. A user submits expense details through a FastAPI API, and the AI agent searches the policy to determine whether the expense follows the rule set.

The system returns:

- compliance status
- clear explanation
- related policy clause
- policy-based guidance

The project uses FastAPI and Swagger UI instead of a separate frontend.

## 2. Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Main programming language |
| FastAPI | Build the backend APIs |
| Swagger UI | Test and use the APIs |
| OpenAI Agents SDK | Create and run the AI agent |
| LangChain | Load and split the policy document |
| Embedding model | Convert policy text into vectors |
| Pinecone | Store and search policy vectors |
| Pydantic | Create input and output models |
| RAG | Retrieve policy information before generating the result |
| Function tool | Allow the AI agent to search the policy |
| Output guardrail | Check that the result includes a policy reference |
| Python-Dotenv | Load API keys from environment variables |

## 3. System Architecture

```text
Company expense policy PDF
  ↓
LangChain document loader
  ↓
Text splitter
  ↓
Embedding model
  ↓
Pinecone vector database
  ↓
Policy knowledge base

User expense details
  ↓
FastAPI API
  ↓
OpenAI agent
  ↓
Policy retrieval function tool
  ↓
Pinecone search
  ↓
Relevant policy rule
  ↓
AI agent decision
  ↓
Output guardrail
  ↓
Structured JSON response
  ↓
Swagger UI
```

## 4. Role of Each Technology

### 4.1 Python

Python is the main programming language for the project. It is used to:

- build the FastAPI backend
- create the AI agent
- process policy documents
- connect to Pinecone
- create tools and guardrails
- handle API requests and responses

### 4.2 FastAPI

FastAPI is used to build the backend APIs. It will:

- receive expense details
- send information to the AI agent
- return the final result as JSON
- provide Swagger UI for testing

The main API endpoints may include:

- `POST /policy/upload`
- `POST /compliance/check`
- `GET /compliance/{id}/clause`
- `GET /policy/versions`
- `GET /health`

### 4.3 Swagger UI

FastAPI provides Swagger UI automatically. It will be used to:

- view available endpoints
- enter expense information
- send API requests
- view JSON responses
- test the project

A separate frontend application will not be created.

### 4.4 OpenAI Agents SDK

The OpenAI Agents SDK is used to create the AI agent. The agent will:

- understand the submitted expense details
- use the policy retrieval tool
- read the retrieved policy information
- compare the expense with the policy
- generate a clear result
- explain the result in simple language

The agent will not create or assume policy rules.

### 4.5 LangChain

LangChain is used to prepare the company policy document for RAG. It will:

- load the policy PDF
- read the policy text
- split the policy into smaller text chunks
- attach useful metadata to the chunks

### 4.6 Text chunking

The company policy may be long and will be divided into smaller text chunks. Each chunk may contain:

- policy text
- policy section
- policy clause
- page number
- policy version
- effective date

Chunking helps the system locate the correct policy information.

### 4.7 Embeddings

The embedding model converts each policy text chunk into a vector. These vectors help the system find policy information related to the user’s expense. The same model is used to convert the expense query into a vector before searching Pinecone.

### 4.8 Pinecone

Pinecone is used as the vector database. It stores:

- policy text chunks
- text embeddings
- section information
- clause information
- page numbers
- policy version
- effective date

When an expense is submitted, Pinecone returns the most relevant policy information.

### 4.9 RAG

RAG stands for Retrieval-Augmented Generation. The system first retrieves relevant company policy information and then gives that information to the AI agent to generate the final answer.

RAG flow:

```text
Expense details
  ↓
Search company policy
  ↓
Get relevant policy rule
  ↓
Give policy rule to AI agent
  ↓
Generate policy-based result
```

### 4.10 Function tool

A Python function is created as a function tool. The AI agent uses this tool to search Pinecone for the relevant policy rule.

The function tool will:

- receive the expense information or search query
- create an embedding
- search Pinecone
- return the most relevant policy chunks
- return policy details such as clause and page number

### 4.11 Pydantic

Pydantic is used to create structured input and output models.

The input model may include:

- expense category
- expense amount
- currency
- expense date
- business purpose
- receipt availability

The output model may include:

- compliance status
- explanation
- policy reference
- policy clause
- policy limit
- extra amount
- missing information
- future guidance

### 4.12 Structured output

The AI agent returns a structured result instead of a plain text response.

Example:

```json
{
  "status": "Non-Compliant",
  "explanation": "The meal expense is above the allowed limit.",
  "policy_reference": "Section 3.2",
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "guidance": "Keep future meal expenses within the approved limit."
}
```

### 4.13 Output guardrail

An output guardrail checks the AI agent result before it is returned to the user.
The guardrail will check:
Is a policy reference included?
Is the result based on retrieved policy information?
Is the policy clause missing?
If a policy-based verdict does not contain a valid policy reference, the result will be rejected.

5. Main System Flow
   Step 1: Upload the Policy
   The company expense policy PDF will be uploaded to the system.
   Step 2: Process the Policy
   The system will:
   Load the PDF
   Extract the text
   Split the text into chunks
   Create embeddings
   Store the embeddings and policy information in Pinecone
   Step 3: Submit an Expense
   The user will submit expense information through the FastAPI API.
   Example:
   {
   "expense_category": "Meal",
   "amount": 7000,
   "currency": "PKR",
   "expense_date": "2026-08-01",
   "business_purpose": "Client dinner",
   "receipt_available": true
   }

Step 4: Search the Policy
The AI agent will use the policy retrieval function tool.
The tool will search Pinecone and return the related policy rule.
Step 5: Check the Expense
The AI agent will compare the expense details with the retrieved policy rule.
Step 6: Generate the Result
The AI agent will return one of these results:
Compliant
Non-Compliant
Needs Approval
If no clear policy rule is found, the system will return:
Policy is silent on this.
Step 7: Check the Result
The output guardrail will check that the result contains a policy reference.
Step 8: Return the Response
FastAPI will return the final result as a structured JSON response.
The response can be viewed and tested in Swagger UI.

6. API Design
   6.1 Upload Policy
   Endpoint:
   POST /policy/upload
   Purpose:
   Upload and process the company expense policy document.

6.2 Check Expense Compliance
Endpoint:
POST /compliance/check
Purpose:
Check an expense against the company policy.
Input:
{
"expense_category": "Meal",
"amount": 7000,
"currency": "PKR",
"expense_date": "2026-08-01",
"business_purpose": "Client dinner",
"receipt_available": true
}

Output:
{
"status": "Non-Compliant",
"explanation": "The meal expense is above the policy limit.",
"policy_reference": "Section 3.2",
"policy_limit": 5000,
"submitted_amount": 7000,
"extra_amount": 2000,
"guidance": "Keep future meal expenses within the approved limit."
}

6.3 Get Policy Clause
Endpoint:
GET /compliance/{id}/clause
Purpose:
Return the policy clause used for the compliance result.

6.4 Get Policy Versions
Endpoint:
GET /policy/versions
Purpose:
Return available policy versions and their effective dates.

6.5 Health Check
Endpoint:
GET /health
Purpose:
Check whether the API is running.
Output:
{
"status": "ok"
}

7. Data Storage
   The first version will use Pinecone to store:
   Policy text chunks
   Policy embeddings
   Policy metadata
   The project will not require a separate database in the first version.
   Expense claim history will not be stored permanently in the first version.

1. Security
   API keys will not be written directly in the code.
   The project will use a .env file to store:
   OpenAI or model API key
   Pinecone API key
   Pinecone index information
   The .env file will not be uploaded to GitHub.

1. Error Handling
   The system will handle the following cases:
   Policy document is missing
   Policy document cannot be processed
   Expense information is incomplete
   No related policy rule is found
   Pinecone search fails
   AI agent fails
   Policy reference is missing
   Invalid API input is submitted
   The API will return clear error messages.

1. Project Limitations
   The first version will:
   Use a sample company expense policy
   Support selected expense categories
   Use FastAPI Swagger UI instead of a separate frontend
   Not make final approval or payment decisions
   Require human review for unclear or complex cases

1. Final Technical Summary
   The project will use:
   FastAPI + Swagger UI + OpenAI Agents SDK + LangChain + Embeddings + Pinecone + RAG + Pydantic + Function Tools + Output Guardrails
   The complete flow will be:
   Policy PDF
   ↓
   LangChain Loader
   ↓
   Text Chunks
   ↓
   Embeddings
   ↓
   Pinecone

Expense Details
↓
FastAPI
↓
AI Agent
↓
Policy Retrieval Tool
↓
Relevant Policy Rule
↓
Structured Compliance Result
↓
Output Guardrail
↓
JSON Response in Swagger UI
