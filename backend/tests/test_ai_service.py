from app.services.ai_service import AIWorkflowService


def test_finance_request_classification():
    service = AIWorkflowService()
    result = service.analyze_request(
        "A client has delayed invoice approvals because finance managers manually review duplicate vendors."
    )
    assert result.category == "Finance Operations"
    assert result.automation_score > 0.4
    assert "Summary:" in result.structured_response


def test_urgency_detection():
    service = AIWorkflowService()
    result = service.analyze_request(
        "Critical support tickets are blocked and need urgent escalation because SLA deadlines are missed."
    )
    assert result.urgency == "High"
