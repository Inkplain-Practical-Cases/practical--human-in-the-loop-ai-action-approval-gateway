# Handler orchestrates tenant-scoped policy, review, expiry and dry-run execution.
from app.features.feature_pipeline.schemas.request import ActionRequest
from app.features.feature_pipeline.services.service_validate import service_validate
from app.features.feature_pipeline.services.service_policy import service_policy
from app.features.feature_pipeline.services.service_queue import service_queue
def handle_request(body: ActionRequest) -> dict:
    state=service_validate(body.model_dump())
    state=service_policy(state)
    state=service_queue(state)
    return state
