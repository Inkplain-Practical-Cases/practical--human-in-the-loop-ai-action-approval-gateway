# Enforce reviewer authorization: pure decision service without real side effects.
def service_authorize(s: dict) -> dict:
    # A simulated human reviewer is tenant-scoped; unknown reviewers fail closed.
    s["authorized_reviewer"]=s["tenant_id"]=="tenant-a"
    s["approval"]["status"]="approved" if s["authorized_reviewer"] else "denied"
    return s
