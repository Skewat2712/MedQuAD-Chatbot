import streamlit as st
from data_loader import load_medquad_data
from retriever import Retriever
from ner import extract_entities
from utils import highlight_entities

@st.cache_data
def load_data():
    return load_medquad_data('data/MedQuAD/')

@st.cache_resource
def setup_retriever(qa_pairs):
    retriever = Retriever()
    if not retriever.index:
        retriever.create_index(qa_pairs)
    return retriever

# --- Streamlit App Config ---
st.set_page_config(page_title="MedQuAD Chatbot", layout="centered")
st.title("Medical Q&A Chatbot")

# --- Initialize Session State ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Load Data & Setup ---
qa_pairs = load_data()
retriever = setup_retriever(qa_pairs)

# --- Input Area ---
user_input = st.text_input("Enter your medical question & press SUBMIT button:")

if st.button("Submit") and user_input:
    result = retriever.retrieve(user_input)[0]
    question, answer = result
    entities = extract_entities(answer)
    highlighted = highlight_entities(answer, entities)

    # Add to chat history
    st.session_state.history.append({
        "question": user_input,
        "answer": highlighted,
        "entities": entities
    })

# --- Display Chat History ---
if st.session_state.history:
    st.subheader("Chat History")
    for idx, entry in enumerate(reversed(st.session_state.history)):
        st.markdown(f"Q{len(st.session_state.history)-idx}: {entry['question']}")
        st.markdown(f"A: {entry['answer']}")
        with st.expander("Detected Medical Entities"):
            st.json(entry["entities"])
        st.markdown("---")
