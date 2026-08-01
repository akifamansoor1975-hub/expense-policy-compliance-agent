# Rules Document

## Project Title

AI-Powered Expense Policy Compliance Agent

## 1. Agent Rules

The AI agent must:

- read and validate expense details
- search the company expense policy using the policy retrieval tool
- use only retrieved policy information
- compare the expense with the related policy rule
- return a clear status, explanation, policy reference, and future guidance
- identify missing or unclear information
- return the result in the required structured format

## 2. Policy Rules

The company expense policy is the main source of information.

The agent must:

- use the related policy section, clause, page number, version, and effective date when available
- use the policy version that applies to the expense date
- never create, change, assume, or invent a policy rule or expense limit
- never make a policy-based decision without policy evidence
- return `Policy is Silent` when no clear rule is found

## 3. Expense Checking Rules

The agent must check:

- expense category
- expense amount and policy limit
- currency and expense date
- business purpose
- receipt requirement
- approval requirement
- policy exceptions

The agent must not guess missing information or use general knowledge as company policy.

## 4. Status Rules

Use only these statuses:

- `Compliant`
  - Use when the expense follows the policy and all required conditions are met.
- `Non-Compliant`
  - Use when the expense breaks a clear policy rule such as exceeding a limit or missing a required receipt.
- `Needs Approval`
  - Use when approval, human review, or additional information is required.
- `Policy is Silent`
  - Use when the policy has no clear rule or does not provide enough information.

## 5. Missing Information Rules

If important information is missing, the agent must:

- list the missing information
- explain why the expense cannot be fully checked
- ask for the missing information when possible
- return `Needs Approval` if human review is required

## 6. Policy Limit and Guidance Rules

When a policy limit exists, the agent must:

- compare the submitted amount with the policy limit
- calculate the extra amount when applicable
- clearly explain the difference

Future guidance must be:

- based on the company policy
- clear and simple
- helpful for avoiding the same violation again

## 7. Output Rules

The result must include:

- `status`
- `explanation`
- `policy_reference`
- `policy_limit`
- `submitted_amount`
- `extra_amount`
- `missing_information`
- `guidance`

A policy-based result must include a policy reference. If no policy rule exists, the policy reference may be `null`.

## 8. Output Guardrail Rules

Before returning the result, the guardrail must check that:

- the status is valid
- the explanation is included
- the result follows the required schema
- a policy reference is included when a policy rule is used
- no unsupported policy rule or limit was created

The result must be rejected or stopped if these conditions are not met.

## 9. Agent Restrictions

The AI agent must not:

- make the final reimbursement or payment decision
- approve or reject payments
- change the company policy
- create policy rules or limits
- guess missing information
- give unsupported advice

The final decision remains with the finance officer or an authorized employee.

## 10. Final Summary

The agent workflow is:

`Receive Expense → Search Policy → Retrieve Rule → Compare Expense → Generate Status → Explain Result → Give Policy Guidance → Pass Guardrail → Return Structured Response`
