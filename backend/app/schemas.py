from datetime import datetime
from pydantic import BaseModel, Field


class WorkflowAnalyzeRequest(BaseModel):
    request_text: str = Field(..., min_length=25, description="Business request or client workflow description")


class WorkflowAnalysis(BaseModel):
    summary: str
    category: str
    urgency: str
    sentiment: str
    automation_score: float
    structured_response: str
    evaluation_score: float
    suggested_next_steps: list[str]


class WorkflowRecordResponse(WorkflowAnalysis):
    id: int
    request_text: str
    created_at: datetime

    model_config = {"from_attributes": True}


class EvaluationRequest(BaseModel):
    request_text: str
    generated_response: str


class EvaluationResponse(BaseModel):
    completeness: float
    structure_quality: float
    actionability: float
    consistency: float
    overall_score: float
    recommendations: list[str]
