
import re
import time
from urllib.parse import urlparse


PATTERNS = [
    {
        "category": "Credential Theft",
        "weight": 30,
        "patterns": [
            r"\botp\b",
            r"\bone.time.password\b",
            r"\bpassword\b",
            r"\batm pin\b",
            r"\bpin\b",
            r"\bcvv\b",
            r"\bshare your otp\b",
            r"\benter your otp\b",
            r"\bprovide your otp\b",
            r"\baccount number\b",
            r"\bcard details\b"
        ],
        "reason": "The message requests sensitive banking or login information."
    },
    {
        "category": "Urgency",
        "weight": 15,
        "patterns": [
            r"\burgent\b",
            r"\bimmediately\b",
            r"\bwithin \d+ minutes?\b",
            r"\bwithin \d+ hours?\b",
            r"\bact now\b",
            r"\bimmediate action required\b",
            r"\bwithout delay\b",
            r"\bfinal warning\b",
            r"\b15 minutes\b"
        ],
        "reason": "The message pressures the recipient to act quickly."
    },
    {
        "category": "Threat or Account Suspension",
        "weight": 20,
        "patterns": [
            r"\baccount.*blocked\b",
            r"\baccount.*suspended\b",
            r"\bpermanent(?:ly)? blocked\b",
            r"\baccount.*restricted\b",
            r"\baccount suspension\b",
            r"\blegal action\b",
            r"\bpermanently blocked\b",
            r"\bservice.*disconnected\b"
        ],
        "reason": "The message threatens account restrictions or consequences."
    },
    {
        "category": "Payment Request",
        "weight": 20,
        "patterns": [
            r"\bpay\b",
            r"\bpayment\b",
            r"\bprocessing fee\b",
            r"\breactivation fee\b",
            r"\btransfer money\b",
            r"\bpay now\b",
            r"\b\d+\s*(?:rs|inr|₹)\b",
            r"\bfee immediately\b"
        ],
        "reason": "The message requests money or an unexpected payment."
    },
    {
        "category": "Suspicious Link",
        "weight": 20,
        "patterns": [
            r"https?://\S+",
            r"\bwww\.\S+",
            r"\bclick this link\b",
            r"\bverification link\b",
            r"\bverify now\b",
            r"\bclick below\b",
            r"\blogin here\b"
        ],
        "reason": "The message directs the recipient to a link or verification page."
    },
    {
        "category": "Impersonation",
        "weight": 15,
        "patterns": [
            r"\bbank security department\b",
            r"\bbank representative\b",
            r"\bsecurity department\b",
            r"\bcustomer support\b",
            r"\bgovernment department\b",
            r"\bofficial department\b",
            r"\bdear customer\b"
        ],
        "reason": "The message uses official-sounding identity claims that cannot be verified from the text."
    }
]


def get_analysis_mode(message_or_length):
    length = (
        message_or_length
        if isinstance(message_or_length, int)
        else len(message_or_length)
    )

    if length <= 100:
        return "Quick Analysis"
    elif length <= 500:
        return "Standard Analysis"
    elif length <= 2000:
        return "Detailed Analysis"
    elif length <= 5000:
        return "Extended Analysis"
    return "Long Message Analysis"


def detect_indicators(message):
    findings = []
    text = message.lower()

    for item in PATTERNS:
        matches = []

        for pattern in item["patterns"]:
            found = re.findall(pattern, text, re.IGNORECASE)
            matches.extend(found)

        if matches:
            unique_matches = list(dict.fromkeys(matches))

            findings.append({
                "category": item["category"],
                "matched_text": ", ".join(unique_matches[:4]),
                "weight": item["weight"],
                "reason": item["reason"]
            })

    return findings


def calculate_score(message, findings):
    score = sum(item["weight"] for item in findings)

    categories = {item["category"] for item in findings}
    text = message.lower()

    # Combination bonuses
    if "Credential Theft" in categories and "Suspicious Link" in categories:
        score += 10

    if "Payment Request" in categories and "Urgency" in categories:
        score += 10

    if "Threat or Account Suspension" in categories and "Urgency" in categories:
        score += 10

    if (
        "Credential Theft" in categories
        and "Threat or Account Suspension" in categories
    ):
        score += 5

    if (
        "Payment Request" in categories
        and "Impersonation" in categories
    ):
        score += 5

    # Explicit requests for sensitive information
    if re.search(
        r"(share|send|provide|enter|submit).{0,35}(otp|password|pin|cvv)",
        text
    ):
        score += 10

    return min(score, 100)


def get_risk_level(score):
    if score >= 80:
        return "Critical"
    elif score >= 60:
        return "High"
    elif score >= 35:
        return "Medium"
    return "Low"


def create_summary(findings, score):
    if not findings:
        return (
            "No strong suspicious wording was detected. "
            "Always verify unexpected requests independently."
        )

    categories = ", ".join(item["category"] for item in findings)

    return (
        f"Detected {len(findings)} warning categories: {categories}. "
        f"The calculated phishing risk score is {score}/100. "
        "Review the detected indicators before taking action."
    )


def create_recommendations(findings):
    categories = {item["category"] for item in findings}

    recommendations = []

    if "Suspicious Link" in categories:
        recommendations.append(
            "Do not open links from unverified messages."
        )

    if "Credential Theft" in categories:
        recommendations.append(
            "Never share OTP, password, PIN or CVV with anyone."
        )

    if "Payment Request" in categories:
        recommendations.append(
            "Do not transfer money or pay unexpected fees."
        )

    if "Threat or Account Suspension" in categories:
        recommendations.append(
            "Verify account status through the official organization."
        )

    recommendations.append(
        "Contact the organization using its official app or website."
    )

    return recommendations


def analyze_with_gemini(message):
    start = time.perf_counter()

    findings = detect_indicators(message)
    score = calculate_score(message, findings)
    risk_level = get_risk_level(score)

    summary = create_summary(findings, score)
    recommendations = create_recommendations(findings)

    elapsed = (time.perf_counter() - start) * 1000

    return {
        "threat_score": score,
        "risk_level": risk_level,
        "summary": summary,
        "flags": findings,
        "next_steps": recommendations,
        "family_advisory": (
            "Warn family members not to share OTPs, passwords "
            "or banking information with unverified senders."
        ),
        "confidence": 90 if findings else 75,
        "analysis_mode": get_analysis_mode(message),
        "processing_time_ms": round(elapsed, 2),
        "injection_blocked": False
    }
