from app.schemas import EvaluationResponse


class WorkflowEvaluator:
    """Simple evaluation layer for generated workflow responses.

    This is intentionally explainable. Recruiters can see how completeness,
    structure, actionability, and consistency are measured before replacing it
    with model-based evaluation or RAGAS-style scoring.
    """

    def evaluate(self, request_text: str, generated_response: str) -> EvaluationResponse:
        response = generated_response.lower()
        completeness = self._score_keywords(response, ["summary", "category", "urgency", "recommended", "workflow"])
        structure_quality = self._score_keywords(response, ["summary:", "workflow category", "recommended response"])
        actionability = self._score_keywords(response, ["automate", "routing", "validation", "review", "store"])
        consistency = 0.9 if len(generated_response) > 100 and len(request_text) > 20 else 0.5
        overall = round((completeness + structure_quality + actionability + consistency) / 4, 2)
        recommendations = []
        if completeness < 0.8:
            recommendations.append("Add clearer summary, category, urgency, and workflow recommendation fields.")
        if actionability < 0.8:
            recommendations.append("Make the output more implementation-focused with concrete next steps.")
        if not recommendations:
            recommendations.append("Response meets the baseline quality checks.")
        return EvaluationResponse(
            completeness=completeness,
            structure_quality=structure_quality,
            actionability=actionability,
            consistency=consistency,
            overall_score=overall,
            recommendations=recommendations,
        )

    def _score_keywords(self, text: str, keywords: list[str]) -> float:
        hits = sum(1 for keyword in keywords if keyword in text)
        return round(hits / len(keywords), 2)
