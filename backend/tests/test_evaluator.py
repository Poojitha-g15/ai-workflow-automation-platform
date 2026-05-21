from app.evaluation.evaluator import WorkflowEvaluator


def test_evaluator_scores_structured_response():
    evaluator = WorkflowEvaluator()
    result = evaluator.evaluate(
        "Automate invoice approvals.",
        "Summary: Invoice approvals are manual. Workflow category: Finance Operations. Recommended response: automate routing, validation, review, and store audit records.",
    )
    assert result.overall_score >= 0.7
