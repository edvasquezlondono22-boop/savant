import requests
import jsonschema
from src.utils.constants import (
    API_CHAT_ENDPOINT,
    FASTAPI_HOST,
    FASTAPI_PORT,
    HELLO_TEXT,
    INTENT_GREET,
    RESPONSE_GREET,
    INTENT_UNKNOWN,
    RESPONSE_UNKNOWN,
    MAX_API_RESPONSE_TIME
)
from src.utils.schemas import SCHEMA_CHAT_RESPONSE

# ---------------------------
# Base URL for API
# ---------------------------
BASE_URL = f"http://{FASTAPI_HOST}:{FASTAPI_PORT}"

# ---------------------------
# Tests
# ---------------------------
def test_chat_api_response_time():
    """
    Validate that the chat endpoint returns a valid response quickly and conforms to the schema.
    """
    # Send POST request with known input
    response = requests.post(f"{BASE_URL}{API_CHAT_ENDPOINT}", json={"text": HELLO_TEXT})

    # ---------------------------
    # Validate HTTP status
    # ---------------------------
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    # ---------------------------
    # Validate response time (max 6 seconds for CI / slow environments)
    # ---------------------------
    assert response.elapsed.total_seconds() < MAX_API_RESPONSE_TIME, (
        f"API response time {response.elapsed.total_seconds():.2f}s exceeded max {MAX_API_RESPONSE_TIME}s"
    )

    # ---------------------------
    # Validate response JSON schema
    # ---------------------------
    jsonschema.validate(response.json(), SCHEMA_CHAT_RESPONSE)

    # ---------------------------
    # Optional: validate actual content of response
    # ---------------------------
    data = response.json()
    if data["intent"] == INTENT_GREET:
        assert data["response"] == RESPONSE_GREET
    else:
        assert data["intent"] == INTENT_UNKNOWN
        assert data["response"] == RESPONSE_UNKNOWN
