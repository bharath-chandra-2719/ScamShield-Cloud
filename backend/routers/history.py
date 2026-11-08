from fastapi import APIRouter, Query
from lib.db import get_history

router = APIRouter()

@router.get("/threat-history")
def threat_history(limit: int = Query(default=50, ge=1, le=200)):
    return get_history(limit)
