# Agentic AI - Mini QA Automation Framework

This repository contains a **mini-framework for automated testing** of a simulated conversational agent system (text and voice). It demonstrates automated **API, E2E conversational flows, and TTS/ASR validation** using Python, Pytest, and Allure.

---

## Table of Contents

* [Technologies](#technologies)
* [Project Structure](#project-structure)
* [Setup](#setup)
* [Running Tests](#running-tests)
* [CI/CD Integration](#ci-cd-integration)
* [Allure Report](#allure-report)
* [Notes](#notes)

---

## Technologies

* Python 3.12
* FastAPI (mock server)
* Pytest, Pytest-HTML, Allure-Pytest
* gTTS, pydub, vosk (voice / ASR)
* JSON Schema validation
* GitHub Actions for CI/CD

---

## Project Structure

```
├─ src/
│  ├─ api_mock.py         # Mock FastAPI server
│  └─ utils/
│      ├─ constants.py    # Constants for tests and API
│      └─ schemas.py      # JSON schemas
├─ tests/
│  ├─ conftest.py         # Pytest fixtures
│  ├─ test_api.py
│  └─ test_voice.py
├─ requirements.txt
├─ .github/workflows/ci.yml
└─ README.md
```

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/savant.git
cd savant
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Install ffmpeg (required for TTS/ASR conversion):

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```

---

## Running Tests

Run all tests locally and generate Allure results:

```bash
pytest --alluredir=reports/allure-results
```

Generate and open Allure HTML report:

```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

---

## CI/CD Integration

* The project uses **GitHub Actions** for CI/CD.
* Tests run automatically on **push or pull request** to the `main` branch.
* Allure results are generated and uploaded as artifacts for each workflow run.

**Badge Example:**

```markdown
![CI](https://github.com/your-username/savant/actions/workflows/ci.yml/badge.svg)
```

* If GitHub Pages is enabled, the Allure report can be viewed online at:
  `https://your-username.github.io/savant/`

---

## Notes

* The FastAPI server is **mocked**, responses are simulated.
* TTS uses **gTTS**, ASR uses **Vosk**.
* JSON schemas validate API responses.
* Constants and endpoints are centralized in `constants.py` for maintainability.
* The project demonstrates **automation best practices**, CI/CD integration, and structured test reporting.
* Voice Model: https://alphacephei.com/vosk/models -> vosk-model-small-en-us-0.15
