# Implementation Plan

## Project Title

AI-Powered Expense Policy Compliance Agent

## 1. Project Setup

The initial implementation steps are:

- create the project folder
- create and activate a Python virtual environment
- install the required packages
- create a `.env` file for API keys
- create the basic FastAPI application

## 2. Project Structure

Create separate folders and files for:

- FastAPI application
- AI agent
- Pydantic schemas
- policy processing
- Pinecone connection
- policy retrieval tool
- guardrails
- API routes
- tests

## 3. Prepare the Company Policy

Implementation tasks:

- add a sample company expense policy PDF
- load the policy with LangChain
- extract the policy text
- split the text into smaller chunks
- add metadata such as section, clause, page number, version, and effective date

## 4. Create the Policy Knowledge Base

Implementation tasks:

- create embeddings for policy chunks
- create a Pinecone index
- store policy embeddings and metadata in Pinecone
- verify that the correct policy rules can be retrieved

## 5. Create Pydantic Schemas

Create models for:

- expense claim input
- policy reference
- compliance result
- policy upload response
- error response

Add validation rules for required fields and valid values.

## 6. Build the Policy Retrieval Tool

Create a Python function tool that:

- receives expense details
- creates a search query
- searches Pinecone
- returns relevant policy rules and metadata

## 7. Create the AI Agent

Use the OpenAI Agents SDK to build the agent. The agent should:

- read the expense details
- use the policy retrieval tool
- compare the expense with the policy
- generate a policy-based result
- explain the result and provide future guidance
- return structured output

## 8. Add Output Guardrails

Create an output guardrail to verify:

- the compliance status is valid
- the explanation is included
- the response matches the required schema
- a policy reference is included when a policy rule is used
- no policy rule or limit is invented

## 9. Build FastAPI Endpoints

Create and connect the following endpoints:

- `POST /policy/upload`
- `POST /compliance/check`
- `GET /compliance/{id}/clause`
- `GET /policy/versions`
- `GET /health`

Connect the endpoints with the AI agent and supporting project services.

## 10. Test the Application

Test the project through Swagger UI using these scenarios:

- compliant expense
- non-compliant expense
- expense above the policy limit
- expense requiring approval
- missing information
- missing receipt
- policy is silent
- invalid input
- policy retrieval failure

## 11. Final Review

Before completion, verify that:

- all API endpoints work
- the correct policy rules are retrieved
- results contain clear explanations and policy references
- the output guardrail works correctly
- API keys are not embedded in the code
- project documentation is updated
- the final demo is prepared

## 12. Implementation Order

```text
Project Setup
  ↓
Policy Processing
  ↓
Embeddings and Pinecone
  ↓
Pydantic Schemas
  ↓
Policy Retrieval Tool
  ↓
AI Agent
  ↓
Output Guardrail
  ↓
FastAPI Endpoints
  ↓
Swagger UI Testing
  ↓
Final Review and Demo
```

## 13. Final Summary

The project will be implemented step by step, beginning with the policy knowledge base. After that, the AI agent, guardrails, and FastAPI APIs will be connected. Finally, the full system will be tested through Swagger UI.
