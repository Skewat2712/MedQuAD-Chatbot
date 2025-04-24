import re

def extract_entities(text):
    # Expanded symptom terms
    symptoms = re.findall(
        r'\b(headache|fever|nausea|pain|cough|fatigue|rash|vomiting|dizziness|sore throat|chills|sweating|shortness of breath|itching|diarrhea|constipation|runny nose|loss of appetite|sneezing|muscle ache|weakness|insomnia)\b',
        text, re.IGNORECASE)

    # Expanded disease terms
    diseases = re.findall(
        r'\b(cancer|diabetes|asthma|flu|covid-19|infection|arthritis|hypertension|pneumonia|tuberculosis|epilepsy|malaria|anemia|hepatitis|alzheimer\'s|stroke|depression|anxiety|migraine|allergy|bronchitis|chickenpox)\b',
        text, re.IGNORECASE)

    # Expanded treatment terms
    treatments = re.findall(
        r'\b(chemotherapy|radiation|medication|surgery|therapy|vaccine|antibiotics|analgesics|immunotherapy|dialysis|physiotherapy|transplant|injection|rehabilitation|antivirals|painkillers|insulin|oxygen therapy|laser therapy)\b',
        text, re.IGNORECASE)

    return {
        'Symptoms': list(set([s.lower() for s in symptoms])),
        'Diseases': list(set([d.lower() for d in diseases])),
        'Treatments': list(set([t.lower() for t in treatments]))
    }
