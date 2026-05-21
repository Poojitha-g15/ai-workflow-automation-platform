# Architecture

```text
React UI
  |
  | REST API
  v
FastAPI Backend
  |
  |-- AIWorkflowService
  |     |-- Prompt templates
  |     |-- OpenAI/Claude provider layer
  |     |-- Local fallback mode
  |
  |-- WorkflowEvaluator
  |     |-- Completeness score
  |     |-- Structure score
  |     |-- Actionability score
  |     |-- Consistency score
  |
  v
PostgreSQL
```

## Design choices

### FastAPI backend
FastAPI keeps the backend clean and easy to document through OpenAPI at `/docs`.

### React frontend
The frontend demonstrates the full user workflow: submit request, analyze, review output, and view saved workflow history.

### PostgreSQL
Workflow records are persisted so the app behaves like a real business workflow platform rather than a stateless demo.

### AI provider abstraction
The AI logic is isolated in `AIWorkflowService`, so OpenAI, Claude, or other model providers can be added without changing the API or UI.

### Evaluation layer
The evaluator makes the project stronger for AI roles because it shows how generated responses are measured and improved.
