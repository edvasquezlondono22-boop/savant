# ---------------------------
# JSON Schemas for API validation
# ---------------------------

SCHEMA_CHAT_RESPONSE = {
    "type": "object",
    "properties": {
        "intent": {"type": "string"},
        "response": {"type": "string"}
    },
    "required": ["intent", "response"]
}
