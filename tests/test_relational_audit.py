"""Verify persistent action HTTP request/outcome foreign key."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_action_audit_relations(tmp_path):
    path=str(tmp_path/"approval.sqlite3")
    request_id=provider_record_request_audit("POST","/actions",202,4.5,path)
    with sqlite3.connect(path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM approval_api_requests WHERE id=?",(request_id,)).fetchone()[0]==1
        assert connection.execute("SELECT COUNT(*) FROM approval_api_events WHERE request_id=?",(request_id,)).fetchone()[0]==1
        assert connection.execute("PRAGMA foreign_key_check").fetchall()==[]
