import { useEffect, useMemo, useState } from 'react';
import { analyzeWorkflow, fetchWorkflows } from './api.js';

const sampleRequest =
  'A client reported that invoice approvals are delayed because finance managers are manually reviewing duplicate vendor records. They want a workflow that flags duplicates, routes high-risk invoices for review, and sends status updates automatically.';

function App() {
  const [requestText, setRequestText] = useState(sampleRequest);
  const [analysis, setAnalysis] = useState(null);
  const [workflows, setWorkflows] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const metrics = useMemo(() => {
    const total = workflows.length;
    const highUrgency = workflows.filter((item) => item.urgency === 'High').length;
    const averageAutomation = total
      ? workflows.reduce((sum, item) => sum + item.automation_score, 0) / total
      : 0;
    return { total, highUrgency, averageAutomation: averageAutomation.toFixed(2) };
  }, [workflows]);

  async function loadWorkflows() {
    try {
      const records = await fetchWorkflows();
      setWorkflows(records);
    } catch (err) {
      console.warn(err.message);
    }
  }

  useEffect(() => {
    loadWorkflows();
  }, []);

  async function handleAnalyze(event) {
    event.preventDefault();
    setLoading(true);
    setError('');
    try {
      const result = await analyzeWorkflow(requestText);
      setAnalysis(result);
      await loadWorkflows();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page-shell">
      <section className="hero">
        <p className="eyebrow">AI workflow automation</p>
        <h1>Analyze requests, classify tasks, and generate structured workflow responses.</h1>
        <p>
          A full-stack portfolio project using React, FastAPI, PostgreSQL, REST APIs, and AI-style prompt workflows.
        </p>
      </section>

      <section className="grid">
        <form className="card input-card" onSubmit={handleAnalyze}>
          <label htmlFor="requestText">Business request</label>
          <textarea
            id="requestText"
            value={requestText}
            onChange={(event) => setRequestText(event.target.value)}
            rows="10"
          />
          <button disabled={loading}>{loading ? 'Analyzing...' : 'Analyze Workflow'}</button>
          {error && <p className="error">{error}</p>}
        </form>

        <section className="card">
          <h2>Workflow metrics</h2>
          <div className="metric-grid">
            <div><span>{metrics.total}</span><p>Total workflows</p></div>
            <div><span>{metrics.highUrgency}</span><p>High urgency</p></div>
            <div><span>{metrics.averageAutomation}</span><p>Avg. automation score</p></div>
          </div>
        </section>
      </section>

      {analysis && (
        <section className="card result-card">
          <div className="result-header">
            <h2>Generated analysis</h2>
            <span className="badge">Score {analysis.evaluation_score}</span>
          </div>
          <div className="pill-row">
            <span>{analysis.category}</span>
            <span>{analysis.urgency} urgency</span>
            <span>{analysis.sentiment}</span>
            <span>Automation {analysis.automation_score}</span>
          </div>
          <h3>Summary</h3>
          <p>{analysis.summary}</p>
          <h3>Structured response</h3>
          <pre>{analysis.structured_response}</pre>
          <h3>Suggested next steps</h3>
          <ul>
            {analysis.suggested_next_steps?.map((step) => <li key={step}>{step}</li>)}
          </ul>
        </section>
      )}

      <section className="card">
        <h2>Recent workflow records</h2>
        <div className="table">
          {workflows.map((workflow) => (
            <div className="table-row" key={workflow.id}>
              <strong>{workflow.category}</strong>
              <span>{workflow.urgency}</span>
              <span>{workflow.automation_score}</span>
              <p>{workflow.summary}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}

export default App;
