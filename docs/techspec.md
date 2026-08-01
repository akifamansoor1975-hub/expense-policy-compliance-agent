Technical Specification Document
Project Title
AI-Powered Expense Policy Compliance Agent

1. Introduction
This document explains how the AI-Powered Expense Policy Compliance Agent will be built.
The system will use a company expense policy document as its main source of information. A user will submit expense details through a FastAPI API.
The AI agent will search the company policy, find the related rule, and check whether the expense follows the policy.
The system will return:
Compliance status
Clear explanation
Related policy clause
Policy-based guidance
The project will use FastAPI and Swagger UI instead of a separate frontend.

2. Technology Stack
The project will use the following technologies:
Technology
Purpose
Python
Main programming language
FastAPI
Build the backend APIs
Swagger UI
Test and use the APIs
OpenAI Agents SDK
Create and run the AI agent
LangChain
Load and split the policy document
Embedding Model
Convert policy text into vectors
Pinecone
Store and search policy vectors
Pydantic
Create input and output models
RAG
Find policy information before generating an answer
Function Tool
Allow the AI agent to search the policy
Output Guardrail
Check that the result contains a policy reference
Python-Dotenv
Load API keys from environment variables


3. System Architecture
The system will follow this flow:
Company Expense Policy PDF
            ↓
LangChain Document Loader
            ↓
Text Splitter
            ↓
Embedding Model
            ↓
Pinecone Vector Database
            ↓
      Policy Knowledge Base


User Expense Details
            ↓
FastAPI API
            ↓
OpenAI Agent
            ↓
Policy Retrieval Function Tool
            ↓
Pinecone Search
            ↓
Relevant Policy Rule
            ↓
AI Agent Decision
            ↓
Output Guardrail
            ↓
Structured JSON Response
            ↓
Swagger UI


4. Role of Each Technology
4.1 Python
Python will be the main programming language for the complete project.
Python will be used to:
Build the FastAPI backend
Create the AI agent
Process policy documents
Connect to Pinecone
Create tools and guardrails
Handle API requests and responses

4.2 FastAPI
FastAPI will be used to build the backend APIs.
FastAPI will:
Receive expense details
Send the expense information to the AI agent
Return the final result as JSON
Provide Swagger UI for testing the APIs
The main API endpoints may include:
POST /policy/upload
POST /compliance/check
GET /compliance/{id}/clause
GET /policy/versions
GET /health

4.3 Swagger UI
FastAPI provides Swagger UI automatically.
Swagger UI will be used to:
View available API endpoints
Enter expense information
Send API requests
View JSON responses
Test the project
A separate frontend application will not be created.

4.4 OpenAI Agents SDK
The OpenAI Agents SDK will be used to create the AI agent.
The AI agent will:
Understand the submitted expense details
Use the policy retrieval tool
Read the retrieved policy information
Compare the expense with the policy
Generate a clear result
Explain the result in simple language
The agent will not create or assume policy rules.

4.5 LangChain
LangChain will be used to prepare the company policy document for RAG.
LangChain will:
Load the policy PDF
Read the policy text
Split the policy into smaller text chunks
Add useful document information to the chunks

4.6 Text Chunking
The company policy may be long. It will be divided into smaller parts called chunks.
Each chunk may contain:
Policy text
Policy section
Policy clause
Page number
Policy version
Effective date
Chunking will help the system find the correct policy information.

4.7 Embeddings
The embedding model will convert each policy text chunk into a vector.
These vectors will help the system find policy information that is related to the user’s expense.
The same embedding model will also convert the expense query into a vector before searching Pinecone.

4.8 Pinecone
Pinecone will be used as the vector database.
Pinecone will store:
Policy text chunks
Text embeddings
Policy section information
Policy clause information
Page numbers
Policy version
Effective date
When an expense is submitted, Pinecone will return the most relevant policy information.

4.9 RAG
RAG means Retrieval-Augmented Generation.
The system will first retrieve relevant information from the company policy. The AI agent will then use that information to generate the result.
The AI agent will not answer only from its general knowledge.
RAG flow:
Expense Details
      ↓
Search Company Policy
      ↓
Get Relevant Policy Rule
      ↓
Give Policy Rule to AI Agent
      ↓
Generate Policy-Based Result


4.10 Function Tool
A Python function will be created as a function tool.
The AI agent will use this tool to search Pinecone for the related policy rule.
The function tool will:
Receive the expense information or search query.
Create an embedding.
Search Pinecone.
Return the most relevant policy chunks.
Return policy details such as the clause and page number.
The AI agent will use the returned information to make its decision.

4.11 Pydantic
Pydantic will be used to create structured input and output models.
The input model may include:
Expense category
Expense amount
Currency
Expense date
Business purpose
Receipt availability
The output model may include:
Compliance status
Explanation
Policy reference
Policy clause
Policy limit
Extra amount
Missing information
Future guidance

4.12 Structured Output
The AI agent will return a structured result instead of a normal text response.
Example:
{
  "status": "Non-Compliant",
  "explanation": "The meal expense is above the allowed limit.",
  "policy_reference": "Section 3.2",
  "policy_limit": 5000,
  "submitted_amount": 7000,
  "extra_amount": 2000,
  "guidance": "Keep future meal expenses within the approved limit."
}


4.13 Output Guardrail
An output guardrail will check the AI agent’s result before it is returned to the user.
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

8. Security
API keys will not be written directly in the code.
The project will use a .env file to store:
OpenAI or model API key
Pinecone API key
Pinecone index information
The .env file will not be uploaded to GitHub.

9. Error Handling
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

10. Project Limitations
The first version will:
Use a sample company expense policy
Support selected expense categories
Use FastAPI Swagger UI instead of a separate frontend
Not make final approval or payment decisions
Require human review for unclear or complex cases

11. Final Technical Summary
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

