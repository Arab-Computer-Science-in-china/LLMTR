from pydantic import BaseModel

class Assistants(BaseModel):
    creator: str
    name: str
    instructions: str
    tools: str
    model: str