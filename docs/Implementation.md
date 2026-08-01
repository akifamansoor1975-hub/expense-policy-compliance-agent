Implementation Planing
Project Title
AI-Powered Expense Policy Compliance Agent
1. Project Setup
Create the project folder.
Create and activate a Python virtual environment.
Install the required packages.
Create a .env file for API keys.
Create the basic FastAPI application.

2. Create the Project Structure
Create separate folders and files for:
FastAPI application
AI agent
Pydantic schemas
Policy processing
Pinecone connection
Policy retrieval tool
Guardrails
API routes
Tests

3. Prepare the Company Policy
Add a sample company expense policy PDF.
Load the policy using LangChain.
Extract the policy text.
Split the text into smaller chunks.
Add policy metadata, such as section, clause, page number, version, and effective date.

4. Create the Policy Knowledge Base
Create embeddings for the policy chunks.
Create a Pinecone index.
Store the policy embeddings and metadata in Pinecone.
Test whether the correct policy rules can be retrieved.

5. Create Pydantic Schemas
Create models for:
Expense claim input
Policy reference
Compliance result
Policy upload response
Error response
Add validation rules for required fields and valid values.

6. Build the Policy Retrieval Tool
Create a Python function tool that will:
Receive expense details.
Create a search query.
Search Pinecone.
Return relevant policy rules and metadata.

7. Create the AI Agent
Use the OpenAI Agents SDK to create the AI agent.
The agent will:
Read the expense details.
Use the policy retrieval tool.
Compare the expense with the policy.
Generate a policy-based result.
Explain the result and provide future guidance.
Return structured output.

8. Add Output Guardrails
Create an output guardrail to check:
The compliance status is valid.
The explanation is included.
The response follows the required schema.
A policy reference is included when a policy rule is used.
No policy rule or limit is invented.

9. Build FastAPI Endpoints
Create and connect these endpoints:
POST /policy/upload
POST /compliance/check
GET /compliance/{id}/clause
GET /policy/versions
GET /health
Connect the endpoints with the AI agent and project services.

10. Test the Application
Test the project using Swagger UI.
Test these cases:
Compliant expense
Non-Compliant expense
Expense above the policy limit
Expense requiring approval
Missing information
Missing receipt
Policy is silent
Invalid input
Policy retrieval failure

11. Final Review
Check that all API endpoints work.
Check that the correct policy rules are retrieved.
Check that results contain clear explanations and policy references.
Check that the output guardrail works.
Check that API keys are not included in the code.
Update the project documentation.
Prepare the final project demonstration.

12. Implementation Order
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

13. Final Summary
The project will be built step by step, starting with the policy knowledge base. Then the AI agent, guardrails, and FastAPI APIs will be connected. Finally, the complete system will be tested in Swagger UI.
