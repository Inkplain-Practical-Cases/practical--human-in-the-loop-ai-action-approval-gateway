# Queue pending approval request: pure decision service without real side effects.
def service_queue(s: dict) -> dict:
    # Stable request IDs ensure repeated messages reference the same decision.
    s["approval"]={"request_id":s["action_id"],"status":"pending","tenant_id":s["tenant_id"]}
    return s
