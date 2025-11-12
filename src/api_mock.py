from fastapi import FastAPI
from pydantic import BaseModel
from src.utils.constants import (
    HELLO_TEXT,
    INTENT_GREET,
    INTENT_UNKNOWN,
    RESPONSE_GREET,
    RESPONSE_UNKNOWN,
    API_CHAT_ENDPOINT
)

# ---------------------------
# FastAPI app
# ---------------------------
app = FastAPI()

class Message(BaseModel):
    text: str

@app.post(API_CHAT_ENDPOINT)
def chat(msg: Message):
    user_input = msg.text.lower()
    
    if user_input == HELLO_TEXT:
        return {"intent": INTENT_GREET, "response": RESPONSE_GREET}
    
    return {"intent": INTENT_UNKNOWN, "response": RESPONSE_UNKNOWN}
