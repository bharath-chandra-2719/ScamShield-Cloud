from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=10_000)

class Indicator(BaseModel):
    label: str = "Warning sign"
    phrase: str
    reason: str

class Verdict(BaseModel):
    threat_score: int = Field(ge=0, le=100)
    threat_category: str
    risk_level: str
    explanation: str
    extracted_indicators: list[Indicator] = Field(default_factory=list)
    safe_next_steps: list[str] = Field(default_factory=list)
    model_confidence: int = Field(default=70, ge=0, le=100)
    injection_blocked: bool = False
