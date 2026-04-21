import json
from db import conn, cursor
from extraction import extract_clinical_data
from evaluation import assess_extraction_quality

# fake transcription (for now)
def transcribe_audio(audio_file_path: str):
    return "patient has fever and was given paracetamol 500 mg"

def process_consultation(audio_file_path: str, consultation_id: int):
    transcript = transcribe_audio(audio_file_path)

    clinical_data = extract_clinical_data(transcript)

    status, reasons = assess_extraction_quality(
        transcript,
        clinical_data,
        ["chief_complaint", "vital_signs", "diagnosis", "medications", "follow_up"]
    )

    cursor.execute("""
    INSERT OR REPLACE INTO consultations (id, status, transcript, clinical_data, reasons)
    VALUES (?, ?, ?, ?, ?)
    """, (
        consultation_id,
        status,
        transcript,
        json.dumps(clinical_data),
        json.dumps(reasons)
    ))

    conn.commit()

    return {
        "status": status,
        "transcript": transcript,
        "clinical_data": clinical_data,
        "reasons": reasons
    }