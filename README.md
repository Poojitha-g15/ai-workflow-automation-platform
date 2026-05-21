# AI-Assisted Workflow Automation Platform

A full-stack AI-assisted workflow platform that summarizes requests, classifies task intent and urgency, generates structured responses, and tracks workflow automation metrics for business process scenarios.

This project is designed as a recruiter-friendly portfolio project for Software Engineer, Full-Stack Engineer, AI Engineer, and Backend Engineer roles.

## Why this project matters

Many business teams handle repeated requests through email, support queues, forms, or chat messages. This platform shows how AI can help triage those requests, extract useful fields, classify task type, generate a suggested response, and store the workflow record for review.

It combines practical full-stack engineering with AI workflow design:

- Prompt templates for consistent AI output
- Request summarization and classification
- Structured JSON response generation
- REST API integration between frontend, backend, database, and AI service layer
- PostgreSQL persistence
- Data-quality and response evaluation
- AWS-ready deployment notes

## Tech Stack

**Frontend:** React, Vite, JavaScript, CSS  
**Backend:** Python, FastAPI, SQLAlchemy, Pydantic  
**Database:** PostgreSQL  
**AI Providers:** OpenAI or Claude-compatible service layer, with local fallback mode  
**DevOps:** Docker, Docker Compose, AWS deployment guide  
**Testing/Evaluation:** Pytest, rule-based evaluation metrics

## Features

- Submit a business request from the React UI
- Summarize long request text into a concise business summary
- Classify request category, urgency, sentiment, and automation opportunity
- Generate a structured response draft for client-style workflows
- Store workflow records in PostgreSQL
- View previous workflow requests in an operations dashboard
- Evaluate AI outputs for completeness, consistency, and formatting quality
- Run locally with or without an AI API key

## Project Structure

```text
workflow-ai-automation-platform/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routers/
│   │   ├── services/
│   │   └── evaluation/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── docs/
│   ├── architecture.md
│   ├── aws-deployment.md
│   ├── github-push-steps.md
│   └── resume-bullets.md
├── docker-compose.yml
├── .env.example
└── README.md
```

## Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/Poojitha-g15/ai-workflow-automation-platform.git
cd ai-workflow-automation-platform
```

### 2. Create environment file

```bash
cp .env.example .env
```

The app works in local fallback mode even without API keys. To use OpenAI or Claude, add your key in `.env`.

### 3. Start with Docker Compose

```bash
docker compose up --build
```

Open:

```text
Frontend: http://localhost:5173
Backend API: http://localhost:8000/docs
```

### 4. Run backend manually

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 5. Run frontend manually

```bash
cd frontend
npm install
npm run dev
```

## Example Workflow Request

```text
A client reported that invoice approvals are delayed because finance managers are manually reviewing duplicate vendor records. They want a workflow that flags duplicates, routes high-risk invoices for review, and sends status updates automatically.
```

Expected output:

- Summary
- Category: Finance Operations
- Urgency: High
- Suggested automation steps
- Response draft
- Evaluation metrics

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check backend health |
| POST | `/api/workflows/analyze` | Analyze and store a workflow request |
| GET | `/api/workflows` | List saved workflow records |
| GET | `/api/workflows/{id}` | Get one workflow record |
| POST | `/api/evaluate` | Evaluate generated response quality |

## Resume Bullets

- Built a full-stack AI-assisted workflow application using Python, React, Node.js tooling, REST APIs, PostgreSQL, and AI model endpoints to summarize requests, classify tasks, generate structured responses, and support business process automation.
- Integrated frontend, backend, database, and AI provider service layers through reusable REST components, validation logic, structured prompt templates, and local fallback handling.
- Applied data science concepts to evaluate AI-generated responses, identify workflow patterns, improve output consistency, and refine prompts for client-style scenarios.

## Suggested GitHub Topics

```text
python
react
fastapi
postgresql
openai
claude
workflow-automation
ai-applications
rest-api
aws
full-stack
```
