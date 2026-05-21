from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class WorkflowRecord(Base):
    __tablename__ = "workflow_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    request_text: Mapped[str] = mapped_column(Text, nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(String(120), nullable=False)
    urgency: Mapped[str] = mapped_column(String(50), nullable=False)
    sentiment: Mapped[str] = mapped_column(String(50), nullable=False)
    automation_score: Mapped[float] = mapped_column(Float, nullable=False)
    structured_response: Mapped[str] = mapped_column(Text, nullable=False)
    evaluation_score: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
