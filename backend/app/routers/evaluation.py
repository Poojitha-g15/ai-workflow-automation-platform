from fastapi import APIRouter
from app.evaluation.evaluator import WorkflowEvaluator
from app.schemas import EvaluationRequest, EvaluationResponse

router = APIRouter(prefix="/api", tags=["evaluation"])
evaluator = WorkflowEvaluator()


@router.post("/evaluate", response_model=EvaluationResponse)
def evaluate_response(payload: EvaluationRequest):
    return evaluator.evaluate(payload.request_text, payload.generated_response)
