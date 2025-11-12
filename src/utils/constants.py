# ---------------------------
# User inputs
# ---------------------------
HELLO_TEXT = "hello"

# ---------------------------
# Intents
# ---------------------------
INTENT_GREET = "greet"
INTENT_UNKNOWN = "unknown"

# ---------------------------
# Responses
# ---------------------------
RESPONSE_GREET = "Hi! How can I help you?"
RESPONSE_UNKNOWN = "Sorry, I didn’t understand."

# ---------------------------
# Voice / TTS
# ---------------------------
TTS_FILE_MP3 = "out.mp3"
TTS_FILE_WAV = "out.wav"
VOSK_MODEL_PATH = "model"

# ---------------------------
# API / Server
# ---------------------------
API_CHAT_ENDPOINT = "/chat"
FASTAPI_HOST = "127.0.0.1"
FASTAPI_PORT = 8000
FASTAPI_DOCS_ENDPOINT = f"http://{FASTAPI_HOST}:{FASTAPI_PORT}/docs"
UVICORN_APP_PATH = "src.api_mock:app"

# ---------------------------
# Process / Test configuration
# ---------------------------
SERVER_START_RETRIES = 10
SERVER_START_SLEEP = 1  # seconds

# ---------------------------
# Messages / Logs
# ---------------------------
LOG_SERVER_STARTED = "✅ FastAPI mock server started successfully."
LOG_SERVER_STOPPED = "🛑 FastAPI server stopped."
LOG_SERVER_FAILED = "❌ Could not start FastAPI server."

# Test / API
MAX_API_RESPONSE_TIME = 0.5  # seconds

# Audio processing
AUDIO_FRAME_CHUNK = 4000  # Number of frames to read per iteration in ASR