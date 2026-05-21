from sqlalchemy.orm import Session
from app.evaluation.evaluator import WorkflowEvaluator
from app.models import WorkflowRecord
from app.schemas import WorkflowAnalysis
from app.services.ai_service import AIWorkflowService


class WorkflowService:
    def __init__(self):
        self.ai_service = AIWorkflowService()
        self.evaluator = WorkflowEvaluator()

    def analyze_and_store(self, db: Session, request_text: str) -> WorkflowRecord:
        ai_result = self.ai_service.analyze_request(request_text)
        evaluation = self.evaluator.evaluate(request_text, ai_result.structured_response)

        record = WorkflowRecord(
            request_text=request_text,
            summary=ai_result.summary,
            category=ai_result.category,
            urgency=ai_result.urgency,
            sentiment=ai_result.sentiment,
            automation_score=ai_result.automation_score,
            structured_response=ai_result.structured_response,
            evaluation_score=evaluation.overall_score,
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    def to_analysis(self, record: WorkflowRecord) -> WorkflowAnalysis:
        return WorkflowAnalysis(
            summary=record.summary,
            category=record.category,
            urgency=record.urgency,
            sentiment=record.sentiment,
            automation_score=record.automation_score,
            structured_response=record.structured_response,
            evaluation_score=record.evaluation_score,
            suggested_next_steps=[],
        )
