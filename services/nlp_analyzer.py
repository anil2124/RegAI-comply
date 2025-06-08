# services/nlp_analyzer.py

import spacy
from spacy.matcher import Matcher

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# --- Rule-Based Matching for NER ---
matcher = Matcher(nlp.vocab)

# Pattern for device names
device_pattern = [
    {"POS": "PROPN"},
    {"IS_UPPER": True, "IS_ALPHA": True},
    {"IS_DIGIT": True, "OP": "?"}
]
matcher.add("DEVICE_NAME", [device_pattern])

# Pattern for defects
defect_pattern = [
    {"LEMMA": {"IN": ["stuck", "broken", "fail", "loose", "crack"]}},
    {"POS": "NOUN", "OP": "+"},
    {"POS": "NOUN", "OP": "*"}
]
matcher.add("DEFECT", [defect_pattern])

# --- NEW: Function for Severity Classification ---
def classify_severity(text: str) -> str:
    """
    Performs a simple keyword-based severity classification.
    """
    text_lower = text.lower()
    # Keywords that indicate a high-priority, serious event
    high_severity_keywords = [
        "death", "serious injury", "hospitalized", "life-threatening",
        "malfunctioned", "permanent impairment"
    ]

    for keyword in high_severity_keywords:
        if keyword in text_lower:
            return "High"
            
    return "Normal"

def analyze_transcript(text: str):
    """
    Analyzes a raw transcript to extract key entities and classify severity.
    """
    doc = nlp(text)
    matches = matcher(doc)
    
    # Get entities
    extracted_entities = {
        "device_name": None,
        "defect": None,
    }
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        if string_id == "DEVICE_NAME":
            extracted_entities["device_name"] = span.text
        elif string_id == "DEFECT":
            extracted_entities["defect"] = span.text

    # --- NEW: Get severity classification ---
    severity = classify_severity(text)
    extracted_entities["severity"] = severity
            
    return extracted_entities
