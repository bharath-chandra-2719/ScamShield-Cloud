import re

MAX_MESSAGE_LENGTH = 10_000

def validate_message(message: str) -> str:
    cleaned = (message or "").strip()
    if not cleaned:
        raise ValueError("Message cannot be empty.")
    if len(cleaned) > MAX_MESSAGE_LENGTH:
        raise ValueError(f"Message must be {MAX_MESSAGE_LENGTH:,} characters or fewer.")
    return cleaned

def extract_urls(text: str) -> list[str]:
    # URL extraction only; this does not establish whether a URL is malicious.
    return re.findall(r"(?:https?://|www\.)[^\s<>'\"]+", text, flags=re.IGNORECASE)
