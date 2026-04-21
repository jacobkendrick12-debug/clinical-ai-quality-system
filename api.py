from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# fake DB
DB: Dict[int, Dict[str, Any]] = {}

# -------------------------
# MOCK PIPELINE COMPONENTS
# -------------------------

def transcribe_audio():
    return "Patient has fever. Prescribed 500mg daily."

def extract_clinical_data(transcript: str):
    return {
        "chief_complaint": "fever",
        "vital_signs": None,
        "diagnosis": None,
        "medications": None,
        "follow_up": None,
        "dosage": "500mg"
    }

# -------------------------
# 🔥 QUALITY LOGIC (REAL)
# -------------------------

def assess_extraction_quality(data: Dict[str, Any]):
    reasons = []
    status = "complete"

    required_fields = [
        "chief_complaint",
        "diagnosis",
        "medications"
    ]

    # Missing fields
    for field in required_fields:
        if not data.get(field):
            reasons.append(f"Missing {field}")

    # Dangerous rule
    if data.get("dosage") and not data.get("medications"):
        reasons.append("Dosage mentioned without medication")
        status = "dangerous"

    # Final status logic
    if status != "dangerous":
        if len(reasons) > 0:
            status = "needs_review"
        else:
            status = "complete"

    return status, reasons

# -------------------------
# 🚀 PROCESS ENDPOINT
# -------------------------

@app.post("/consultations/{id}/process")
def process_consultation(id: int):
    transcript = transcribe_audio()
    data = extract_clinical_data(transcript)

    status, reasons = assess_extraction_quality(data)

    DB[id] = {
        "status": status,
        "transcript": transcript,
        "clinical_data": data,
        "reasons": reasons
    }

    return {"message": "processing complete"}

# -------------------------
# 📊 RESULT ENDPOINT
# -------------------------

@app.get("/consultations/{id}/result")
def get_result(id: int):
    return DB.get(id, {"status": "not_found"})