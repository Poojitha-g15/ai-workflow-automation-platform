from __future__ import annotations

import re
from dataclasses import dataclass
from app.config import settings


@dataclass
class AIWorkflowResult:
    summary: str
    category: str
    urgency: str
    sentiment: str
    automation_score: float
    structured_response: str
    suggested_next_steps: list[str]


class AIWorkflowService:
    """AI provider abstraction.

    The project is designed to work in two modes:
    1. Local fallback mode for recruiters and local demos without API keys.
    2. Provider mode where OpenAI or Claude calls can be added behind this class.
    """

    def analyze_request(self, request_text: str) -> AIWorkflowResult:
        if settings.ai_provider.lower() in {"openai", "anthropic"} and not settings.local_fallback_mode:
            # Placeholder for real provider call. Keeping this isolated makes the project easy to extend.
            return self._fallback_analyze(request_text)
        return self._fallback_analyze(request_text)

    def _fallback_analyze(self, request_text: str) -> AIWorkflowResult:
        text = request_text.strip()
        lower = text.lower()
        category = self._classify_category(lower)
        urgency = self._classify_urgency(lower)
        sentiment = self._classify_sentiment(lower)
        automation_score = self._score_automation(lower)
        summary = self._summarize(text)
        response = self._generate_response(summary, category, urgency, automation_score)
        next_steps = self._next_steps(category, urgency)
        return AIWorkflowResult(
            summary=summary,
            category=category,
            urgency=urgency,
            sentiment=sentiment,
            automation_score=automation_score,
            structured_response=response,
            suggested_next_steps=next_steps,
        )

    def _summarize(self, text: str) -> str:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        first = sentences[0] if sentences else text
        if len(first) > 220:
            first = first[:217].rstrip() + "..."
        return first

    def _classify_category(self, lower: str) -> str:
        if any(word in lower for word in ["invoice", "payment", "vendor", "billing", "finance"]):
            return "Finance Operations"
        if any(word in lower for word in ["ticket", "incident", "sla", "support", "customer"]):
            return "Customer Support"
        if any(word in lower for word in ["hire", "employee", "onboarding", "hr", "candidate"]):
            return "HR Operations"
        if any(word in lower for word in ["inventory", "shipment", "order", "warehouse", "supply"]):
            return "Supply Chain"
        return "General Business Workflow"

    def _classify_urgency(self, lower: str) -> str:
        if any(word in lower for word in ["blocked", "critical", "urgent", "immediately", "outage", "breach"]):
            return "High"
        if any(word in lower for word in ["delay", "manual", "escalate", "risk", "sla"]):
            return "Medium"
        return "Low"

    def _classify_sentiment(self, lower: str) -> str:
        if any(word in lower for word in ["frustrated", "angry", "delayed", "blocked", "issue", "complaint"]):
            return "Concerned"
        if any(word in lower for word in ["improve", "automate", "optimize", "streamline"]):
            return "Constructive"
        return "Neutral"

    def _score_automation(self, lower: str) -> float:
        score = 0.35
        signals = ["manual", "repeated", "approval", "routing", "status", "summarize", "classify", "generate", "automate", "workflow"]
        score += sum(0.07 for s in signals if s in lower)
        return round(min(score, 0.95), 2)

    def _generate_response(self, summary: str, category: str, urgency: str, automation_score: float) -> str:
        return (
            f"Summary: {summary}\n\n"
            f"Workflow category: {category}. Urgency: {urgency}. "
            f"Automation opportunity score: {automation_score}.\n\n"
            "Recommended response: We can automate this workflow by capturing the incoming request, "
            "extracting key fields, classifying the task, routing it based on urgency and category, "
            "and generating a structured response for human review before final submission."
        )

    def _next_steps(self, category: str, urgency: str) -> list[str]:
        steps = [
            "Define required input fields and validation rules.",
            "Create prompt templates for summarization, classification, and response drafting.",
            "Store workflow records in PostgreSQL for reporting and auditability.",
        ]
        if urgency == "High":
            steps.insert(0, "Add high-priority escalation routing and SLA alerts.")
        if category == "Finance Operations":
            steps.append("Add duplicate vendor and invoice-risk checks before approval routing.")
        return steps
