import os
import xml.etree.ElementTree as ET

def load_medquad_data(data_dir):
    qa_pairs = []
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.xml'):
                tree = ET.parse(os.path.join(root, file))
                root_elem = tree.getroot()
                for pair in root_elem.findall(".//QAPair"):
                    question = pair.find("Question").text if pair.find("Question") is not None else ""
                    answer = pair.find("Answer").text if pair.find("Answer") is not None else ""
                    if question and answer:
                        qa_pairs.append((question.strip(), answer.strip()))
    return qa_pairs
