# Evaluate action risk policy: pure decision service without real side effects.
def service_policy(s: dict) -> dict:
    # Sensitive write operations require review; no action executes in this step.
    s["risk"]="high" if s["action_id"].lower().startswith("write") else "medium"
    s["requires_approval"]=True
    return s
