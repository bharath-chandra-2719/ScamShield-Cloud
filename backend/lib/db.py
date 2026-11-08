
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DATABASE_URL = os.getenv("DATABASE_URL")
DB_PATH = os.getenv("DATABASE_PATH", "./scamshield.db")


def is_postgres():
    return bool(DATABASE_URL)


def connect():
    if is_postgres():
        import psycopg
        from psycopg.rows import dict_row

        url = DATABASE_URL

        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql://", 1)

        return psycopg.connect(url, row_factory=dict_row)

    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with connect() as conn:
        if is_postgres():
            conn.execute("""
                CREATE TABLE IF NOT EXISTS analyses (
                    id BIGSERIAL PRIMARY KEY,
                    message TEXT NOT NULL,
                    verdict_json TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
        else:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS analyses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message TEXT NOT NULL,
                    verdict_json TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)

        conn.commit()


def save_analysis(message: str, verdict: dict[str, Any]) -> int:
    created_at = datetime.now(timezone.utc).isoformat()
    verdict_data = json.dumps(verdict)

    with connect() as conn:
        if is_postgres():
            cur = conn.execute(
                """
                INSERT INTO analyses
                (message, verdict_json, created_at)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (message, verdict_data, created_at)
            )
            analysis_id = cur.fetchone()["id"]

        else:
            cur = conn.execute(
                """
                INSERT INTO analyses
                (message, verdict_json, created_at)
                VALUES (?, ?, ?)
                """,
                (message, verdict_data, created_at)
            )
            analysis_id = cur.lastrowid

        conn.commit()
        return int(analysis_id)


def get_history(limit: int = 50) -> list[dict[str, Any]]:
    limit = max(1, min(limit, 100))

    with connect() as conn:
        if is_postgres():
            rows = conn.execute(
                """
                SELECT id, message, verdict_json, created_at
                FROM analyses
                ORDER BY id DESC
                LIMIT %s
                """,
                (limit,)
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT id, message, verdict_json, created_at
                FROM analyses
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,)
            ).fetchall()

    items = []

    for row in rows:
        items.append({
            "id": row["id"],
            "message": row["message"],
            "created_at": row["created_at"],
            **json.loads(row["verdict_json"])
        })

    return items
