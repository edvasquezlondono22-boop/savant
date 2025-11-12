import os
import json
import wave
from gtts import gTTS
from pydub import AudioSegment
import vosk

from src.utils.constants import (
    TTS_FILE_MP3,
    TTS_FILE_WAV,
    VOSK_MODEL_PATH,
    HELLO_TEXT,
    AUDIO_FRAME_CHUNK
)

def test_tts_and_asr():
    """
    Validate that Text-to-Speech (TTS) and Automatic Speech Recognition (ASR) work correctly.
    """

    text = HELLO_TEXT  # Use constant from utils

    # ---------------------------
    # Generate MP3 using gTTS
    # ---------------------------
    tts = gTTS(text)
    tts.save(TTS_FILE_MP3)

    # ---------------------------
    # Convert MP3 to WAV using pydub
    # ---------------------------
    sound = AudioSegment.from_mp3(TTS_FILE_MP3)
    sound.export(TTS_FILE_WAV, format="wav")

    # ---------------------------
    # Open WAV file to verify it's valid
    # ---------------------------
    try:
        wf = wave.open(TTS_FILE_WAV, "rb")
    except Exception as e:
        assert False, f"Failed to open WAV file: {e}"

    # ---------------------------
    # Load Vosk model for ASR
    # ---------------------------
    try:
        model = vosk.Model(VOSK_MODEL_PATH)
    except Exception as e:
        assert False, f"Failed to load Vosk model: {e}"

    rec = vosk.KaldiRecognizer(model, wf.getframerate())

    # Feed audio frames to recognizer
    while True:
        data = wf.readframes(AUDIO_FRAME_CHUNK)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    # Get final recognition result
    result = json.loads(rec.FinalResult())
    print(result)

    # ---------------------------
    # Validate that ASR output contains the original text
    # ---------------------------
    assert text.lower() in result.get("text", "").lower(), (
        f"ASR result does not contain the expected text. Expected '{text}', got '{result.get('text', '')}'"
    )

    # ---------------------------
    # Cleanup generated files
    # ---------------------------
    wf.close()
    os.remove(TTS_FILE_MP3)
    os.remove(TTS_FILE_WAV)
