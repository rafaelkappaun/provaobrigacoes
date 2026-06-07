import uuid
from fastapi import Header, HTTPException

def get_session_id(x_session_id: str = Header(default=None)) -> str:
    if not x_session_id:
        x_session_id = str(uuid.uuid4())
    return x_session_id
