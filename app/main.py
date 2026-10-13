# Application entry point: builds the FastAPI app and mounts the feature router.
from fastapi import FastAPI
from app.features.feature_pipeline.router import router
app = FastAPI(title="Typed agent action intake")
app.include_router(router)

# Persist bounded request/outcome audit independently of action approval logic.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
