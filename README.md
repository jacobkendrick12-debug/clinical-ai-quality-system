# 🏥 Clinical AI Quality Control System

## 📌 Overview
This project implements a clinical AI pipeline that processes consultation data and applies a **quality control layer** to detect incomplete or unsafe outputs before they are used in clinical workflows.

The system demonstrates how AI-generated clinical data should be validated and flagged rather than blindly trusted.

---

## 🚀 Features
- FastAPI backend
- Next.js frontend dashboard
- Simulated pipeline (transcription → extraction → evaluation)
- Structured clinical data extraction (mocked)
- Quality control with safety checks
- Status classification:
  - `complete`
  - `needs_review`
  - `dangerous`
- Explainable reasoning (flags/reasons)
- REST API endpoints

---

## 🧠 System Flow

1. **Transcription (Mocked)**
   - Simulates audio → text conversion

2. **Clinical Data Extraction**
   Extracted fields:
   - chief_complaint
   - vital_signs
   - diagnosis
   - medications
   - follow_up
   - dosage

3. **Quality Evaluation (Core Logic)**
   The system validates extracted data using deterministic rules:

   - Missing required fields → `needs_review`
   - Clinically unsafe conditions → `dangerous`
   - Complete + valid → `complete`

   Example rules:
   - Missing diagnosis → flag
   - Missing medication → flag
   - Dosage without medication → **dangerous**

---

## 📡 API Endpoints

### POST `/consultations/{id}/process`
Runs the pipeline:
- transcription
- extraction
- quality evaluation

### GET `/consultations/{id}/result`
Returns:

```json
{
  "status": "dangerous",
  "transcript": "Patient has fever. Prescribed 500mg daily.",
  "clinical_data": {
    "chief_complaint": "fever",
    "diagnosis": null,
    "medications": null,
    "dosage": "500mg"
  },
  "reasons": [
    "Missing diagnosis",
    "Missing medications",
    "Dosage mentioned without medication"
  ]
} 

Example of unsafe consultation:

Status: dangerous
Reasons:

Missing diagnosis
Missing medications
Dosage mentioned without medication

This demonstrates the system’s ability to detect and block unsafe AI outputs before clinical use.