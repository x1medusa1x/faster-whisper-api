import os
import time
from fastapi import FastAPI, UploadFile, File, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from faster_whisper import WhisperModel
import tempfile

MODEL_DIR = os.environ.get("WHISPER_MODEL_DIR", "./")

api_router = APIRouter()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = WhisperModel("tiny.en", compute_type="int8_float16", device="cuda")
    print("Loaded model with GPU acceleration")
except Exception as e:
    print(f"Failed to load model with CUDA: {e}")
    model = WhisperModel("tiny.en")
    print("Loaded model on CPU")

# Transcription route
@api_router.post("/transcribe")
async def transcribe(audio_file: UploadFile = File(...)):
    start_time = time.time()

    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        tmp.write(await audio_file.read())
        tmp.flush()

        segments, info = model.transcribe(tmp.name)
        result = " ".join([seg.text for seg in segments])

    duration = round(time.time() - start_time, 2)
    print(f"Transcription completed in {duration}s")

    return {
        "success": True,
        "data": {
            "language": info.language,
            "text": result,
            "duration": duration
        }
    }

# Add router
app.include_router(api_router, prefix="/api")
