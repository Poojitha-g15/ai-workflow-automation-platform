from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import WorkflowRecord
from app.schemas import WorkflowAnalyzeRequest, WorkflowRecordResponse
from app.services.ai_service import AIWorkflowService
from app.services.workflow_service import WorkflowService

router = APIRouter(prefix="/api/workflows", tags=["workflows"])
workflow_service = WorkflowService()
ai_service = AIWorkflowService()


@router.post("/analyze", response_model=WorkflowRecordResponse)
def analyze_workflow(payload: WorkflowAnalyzeRequest, db: Session = Depends(get_db)):
    ai_result = ai_service.analyze_request(payload.request_text)
    record = workflow_service.analyze_and_store(db, payload.request_text)
    response = WorkflowRecordResponse.model_validate(record)
    response.suggested_next_steps = ai_result.suggested_next_steps
    return response


@router.get("", response_model=list[WorkflowRecordResponse])
def list_workflows(db: Session = Depends(get_db)):
    records = db.query(WorkflowRecord).order_by(WorkflowRecord.created_at.desc()).limit(50).all()
    return [WorkflowRecordResponse.model_validate(record) for record in records]


@router.get("/{workflow_id}", response_model=WorkflowRecordResponse)
def get_workflow(workflow_id: int, db: Session = Depends(get_db)):
    record = db.query(WorkflowRecord).filter(WorkflowRecord.id == workflow_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Workflow record not found")
    return WorkflowRecordResponse.model_validate(record)
