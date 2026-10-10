# Apply expiration and replay guard: pure decision service without real side effects.
def service_expiry(s: dict) -> dict:
    # No grant is reused after an expired or denied decision.
    s["approval"]["usable"]=s["approval"]["status"]=="approved" and not s.get("expired",False)
    return s
