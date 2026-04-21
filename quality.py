def assess_extraction_quality(transcript, clinical_data, required_fields):
    missing = [f for f in required_fields if not clinical_data.get(f)]

    if not missing:
        return "PASS", ["All fields present"]

    return "FAIL", [f"Missing fields: {missing}"]