# Input contract: Pydantic validates fields at the external boundary.
from pydantic import BaseModel, Field
class ActionRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
    action_id: str = Field(min_length=1)
