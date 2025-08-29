import torch
from transformers import pipeline

class CoachLLM:
    def __init__(self, model_name="google/flan-t5-small"):
        # Detect GPU if available, otherwise use CPU
        device = 0 if torch.cuda.is_available() else -1

        self.generator = pipeline(
            "text2text-generation",
            model=model_name,
            device=device
        )

    def generate_feedback(self, question, answer):
        prompt = f"""
You are an AI Interview Coach. 
Evaluate the candidate's response to the interview question. 
Always provide feedback in the following structure:

Question: {question}
Candidate's Answer: {answer}

Feedback:
✅ Correct Answer (Provide the correct, detailed explanation.)
❌ Mistakes in Candidate Answer (List if any, otherwise say 'No major mistakes.')
💡 Suggestions for Improvement (Give 2-3 specific ways the candidate can improve.)
        """

        response = self.generator(
            prompt,
            max_length=350,
            do_sample=True,
            temperature=0.7,
        )

        feedback = response[0]["generated_text"].replace(prompt, "").strip()
        return feedback
