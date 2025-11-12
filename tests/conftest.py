import subprocess
import time
import pytest
import requests
from src.utils.constants import (
    UVICORN_APP_PATH,
    FASTAPI_PORT,
    FASTAPI_DOCS_ENDPOINT,
    SERVER_START_RETRIES,
    SERVER_START_SLEEP,
    LOG_SERVER_STARTED,
    LOG_SERVER_STOPPED,
    LOG_SERVER_FAILED
)

@pytest.fixture(scope="session", autouse=True)
def start_fastapi_server():
    """
    Start the FastAPI server before running tests and stop it after all tests finish.
    """

    # Launch the server as a background process
    process = subprocess.Popen(
        ["uvicorn", UVICORN_APP_PATH, "--port", str(FASTAPI_PORT)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait until the server is available
    for _ in range(SERVER_START_RETRIES):
        try:
            r = requests.get(FASTAPI_DOCS_ENDPOINT)
            if r.status_code == 200:
                print(LOG_SERVER_STARTED)
                break
        except Exception:
            time.sleep(SERVER_START_SLEEP)
    else:
        process.kill()
        raise RuntimeError(LOG_SERVER_FAILED)

    # Yield control to tests
    yield

    # Stop the server when tests are done
    process.terminate()
    process.wait(timeout=5)
    print(LOG_SERVER_STOPPED)
