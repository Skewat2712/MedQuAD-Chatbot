
#  Medical Q&A Chatbot using MedQuAD Dataset

This is a specialized **Medical Question-Answering Chatbot** built using the [MedQuAD Dataset](https://github.com/abachaa/MedQuAD). The chatbot uses information retrieval, basic medical entity recognition (NER), and a simple Streamlit UI to provide medically relevant answers to user queries.

---

##  Features

-  **Retrieves answers** from a curated set of medical Q&A pairs
-  **Entity Recognition**: Identifies symptoms, diseases, and treatments
-  **Chat History**: Keeps track of user queries and responses
-  **Justified Answer Display** for improved readability
-  **Streamlit Web Interface** for ease of use

---

##  Project Structure

```
MedicalQA_MedQuad/
│
├── data/
│   └── MedQuAD/               # Folder containing XML files from MedQuAD
├── app.py                    # Main Streamlit app
├── data_loader.py            # Loads and parses MedQuAD XML data
├── retriever.py              # Retrieval logic using FAISS
├── ner.py                    # Medical Named Entity Recognition(Symptoms, Diseases, and treatment)
├── utils.py                  # Helper functions (e.g., justify text, highlight entities)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MedicalQA_MedQuad.git
cd MedicalQA_MedQuad
```

### 2. Set Up Virtual Environment 
```bash
python -m venv venv
venv/Scripts/activate  
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download and Place MedQuAD Dataset

Download the MedQuAD dataset from:
[https://github.com/abachaa/MedQuAD](https://github.com/abachaa/MedQuAD)

Extract and place all XML files inside:

```
data/MedQuAD/
```

### 5. Run the App

```bash
streamlit run app.py
```

---

