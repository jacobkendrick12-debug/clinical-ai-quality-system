def assess_extraction_quality(transcript, clinical_data, required_fields):
    missing = []

    for field in required_fields:
        if field not in clinical_data or not clinical_data[field]:
            missing.append(field)

    if not missing:
        return "PASS", ["ALL fields present"]

    return "FAIL", [f"Missing: {missing}"]