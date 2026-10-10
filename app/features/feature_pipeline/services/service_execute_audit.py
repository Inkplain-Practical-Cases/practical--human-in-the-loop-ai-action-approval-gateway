# Execute safely and audit decision: pure decision service without real side effects.
def service_execute_audit(s: dict) -> dict:
    # Educational dry run: never perform a real side-effectful external operation.
    s["execution"]={"performed":bool(s["approval"]["usable"]),"mode":"dry_run"}
    s["audit"]={"tenant_id":s["tenant_id"],"action_id":s["action_id"],"approved":s["approval"]["usable"]}
    return s
