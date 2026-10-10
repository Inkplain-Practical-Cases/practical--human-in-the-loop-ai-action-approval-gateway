from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_approval_capability():
    r=client.post("/actions",json={"tenant_id":"tenant-a","action_id":"write-order"})
    assert r.status_code==200
    assert "authorized_reviewer" in r.json()
def test_invalid_action_blocked():
    assert client.post("/actions",json={"tenant_id":"tenant-a","action_id":""}).status_code==422
