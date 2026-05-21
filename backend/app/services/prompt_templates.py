WORKFLOW_ANALYSIS_TEMPLATE = """
You are an AI workflow automation analyst. Analyze the business request and return a practical structured response.

Request:
{request_text}

Return these fields:
1. Summary
2. Category
3. Urgency
4. Sentiment
5. Automation Opportunity Score from 0 to 1
6. Suggested Workflow Response
7. Next Steps

Keep the response specific, business-friendly, and implementation-oriented.
"""

RESPONSE_EVALUATION_TEMPLATE = """
Evaluate the generated response for completeness, structure, actionability, and consistency.
Request: {request_text}
Generated Response: {generated_response}
"""
