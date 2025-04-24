import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, model_name='all-MiniLM-L6-v2', index_path='embeddings/faiss_index/'):
        self.model = SentenceTransformer(model_name)
        self.index_path = index_path
        self.index = None
        self.qa_pairs = []

        if os.path.exists(index_path + 'faiss.index') and os.path.exists(index_path + 'qa_pairs.pkl'):
            self.load_index()

    def create_index(self, qa_pairs):
        self.qa_pairs = qa_pairs
        questions = [q for q, _ in qa_pairs]
        embeddings = self.model.encode(questions, show_progress_bar=True)
        dim = embeddings[0].shape[0]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        self.index = index
        os.makedirs(self.index_path, exist_ok=True)
        faiss.write_index(index, self.index_path + 'faiss.index')
        with open(self.index_path + 'qa_pairs.pkl', 'wb') as f:
            pickle.dump(self.qa_pairs, f)

    def load_index(self):
        self.index = faiss.read_index(self.index_path + 'faiss.index')
        with open(self.index_path + 'qa_pairs.pkl', 'rb') as f:
            self.qa_pairs = pickle.load(f)

    def retrieve(self, query, k=1):
        query_vec = self.model.encode([query])
        _, indices = self.index.search(query_vec, k)
        return [self.qa_pairs[i] for i in indices[0]]
