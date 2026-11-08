
import traceback
from fastapi import APIRouter, HTTPException

from models.verdict import AnalyzeRequest, Verdict
from lib.security import validate_message
from lib.lm import analyze_with_gemini
from lib.db import save_analysis

router = APIRouter()


@router.post("/analyze-message", response_model=Verdict)
def analyze_message(payload: AnalyzeRequest):

    try:
        # Validate the submitted message
        message = validate_message(payload.message)

        print("\n========== SCAMSHIELD ANALYSIS ==========")
        print("Received message:", message[:150])

        # Perform local rule-based analysis
        result = analyze_with_gemini(message)

        # Convert backend warning flags into frontend indicators
        flags = result.get("flags", [])

        extracted_indicators = []

        for flag in flags:
            extracted_indicators.append({
                "label": flag.get("category", "Warning Sign"),
                "phrase": flag.get("matched_text", ""),
                "reason": flag.get(
                    "reason",
                    "Potentially suspicious wording detected."
                )
            })

        # Get detected threat categories
        categories = [
            flag.get("category", "Warning Sign")
            for flag in flags
        ]

        threat_category = (
            ", ".join(categories)
            if categories
            else "No Threat Detected"
        )

        # Build the complete frontend response
        result["threat_category"] = threat_category

        result["explanation"] = result.get(
            "summary",
            "Analysis completed using suspicious-word and phrase detection."
        )

        result["extracted_indicators"] = extracted_indicators

        result["safe_next_steps"] = result.get(
            "next_steps",
            [
                "Do not click suspicious links.",
                "Never share OTP, password, PIN or CVV.",
                "Verify the message using official channels."
            ]
        )

        result["model_confidence"] = result.get(
            "confidence",
            90
        )

        # Ensure score is within the valid range
        result["threat_score"] = max(
            0,
            min(100, int(result.get("threat_score", 0)))
        )

        # Print results for debugging
        print("Threat score:", result["threat_score"])
        print("Threat category:", result["threat_category"])
        print("Detected red flags:", extracted_indicators)
        print("Analysis mode:", result.get("analysis_mode"))

        # Save the complete analysis
        save_analysis(message, result)

        print("Analysis saved successfully")
        print("========================================\n")

        return result

    except ValueError as exc:
        print("VALIDATION ERROR:", str(exc))
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    except Exception as exc:
        print("BACKEND ERROR:")
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )
