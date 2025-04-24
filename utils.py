import re

def highlight_entities(text, entities_dict):
   
    for category, entities in entities_dict.items():
        for entity in sorted(entities, key=len, reverse=True):  # longer first to avoid partial replacements
            pattern = re.compile(rf'\b({re.escape(entity)})\b', re.IGNORECASE)
            text = pattern.sub(r'**\1**', text)
    return text
