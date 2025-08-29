from sentence_transformers import SentenceTransformer, util
from pathlib import Path


class Evaluator:
    def __init__(self, emb_path: Path):
        self.model = SentenceTransformer(str(emb_path))

    def score(self, reference: str, answer: str) -> float:
        # Encode both texts
        ref_emb = self.model.encode(reference, convert_to_tensor=True)
        ans_emb = self.model.encode(answer, convert_to_tensor=True)
        # Compute cosine similarity
        sim = util.pytorch_cos_sim(ref_emb, ans_emb)
        return float(sim.item())
