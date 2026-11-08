export type Flag = { label: string; phrase: string; reason: string };
export type Verdict = {
  threat_score: number;
  threat_category: string;
  risk_level: string;
  explanation: string;
  extracted_indicators: Flag[] | string[];
  safe_next_steps: string[];
  model_confidence?: number;
  injection_blocked?: boolean;
};

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function analyzeMessage(message: string): Promise<Verdict> {
  const response = await fetch(`${API_BASE}/api/analyze-message`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.detail || `Analysis failed (${response.status})`);
  }
  return response.json();
}

export async function getThreatHistory(): Promise<any[]> {
  const response = await fetch(`${API_BASE}/api/threat-history`);
  if (!response.ok) throw new Error("Could not load threat history");
  return response.json();
}
