const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export async function analyzeWorkflow(requestText) {
  const response = await fetch(`${API_BASE_URL}/api/workflows/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ request_text: requestText })
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || 'Unable to analyze workflow');
  }

  return response.json();
}

export async function fetchWorkflows() {
  const response = await fetch(`${API_BASE_URL}/api/workflows`);
  if (!response.ok) {
    throw new Error('Unable to load workflows');
  }
  return response.json();
}
