# Clinical AI API

## Overview
This project is a simple Clinical AI pipeline that processes consultation audio into structured medical data.

The system simulates how clinical conversations can be transformed into usable healthcare insights.

---

## 🚀 Features
- FastAPI backend
- Audio → transcript (mocked)
- Clinical data extraction
- Quality evaluation (PASS / FAIL)
- SQLite database storage
- REST API endpoints
- Auto-generated API docs

---

## 🧠 System Flow

1. **Transcription**
   - Converts audio into text (currently mocked)

2. **Clinical Extraction**
   - Extracts structured fields:
     - chief complaint
     - vital signs
     - diagnosis
     - medications
     - follow-up

3. **Evaluation**
   - Checks if required fields are present
   - Returns PASS or FAIL with reasons

4. **Storage**
   - Results stored in SQLite database

---

## 📡 API Endpoints

### 1. Process Consultation
**POST** `/consultations/{consultation_id}/process`

- Processes a consultation
- Stores results in DB

---

### 2. Get Consultation Result
**GET** `/consultations/{consultation_id}/result`

Returns:
```json
{
  "status": "PASS",
  "transcript": "patient has fever...",
  "clinical_data": {
    "chief_complaint": "fever",
    "diagnosis": "infection"
  },
  "reasons": ["ALL fields present"]
}

## Example Output

Example of unsafe consultation:

Status: dangerous  
Reasons:
- Missing diagnosis  
- Missing medications  
- Dosage mentioned without medication  

This demonstrates the system’s ability to detect unsafe AI outputs before clinical use.