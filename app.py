from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import bleach
from model import CoachLLM

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))  # Secure secret key

# Use a stronger model
MODEL_PATH = "HuggingFaceH4/zephyr-7b-beta"
coach = CoachLLM(MODEL_PATH)

# Interview Questions
questions = [
    "What is overfitting in machine learning?",
    "Explain the difference between supervised and unsupervised learning.",
    "What is regularization in ML and why is it important?",
    "Can you explain the bias-variance tradeoff?",
    "What is the purpose of cross-validation?",
    "What is the difference between a classifier and a regressor?"
]

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize session variables
    if "q_index" not in session:
        session["q_index"] = 0
        session["answers"] = {}
        session["feedbacks"] = {}

    q_index = session["q_index"]
    question = questions[q_index]
    feedback = session["feedbacks"].get(q_index)
    answer = session["answers"].get(q_index, "")

    if request.method == "POST":
        if "answer" in request.form:  # Submitted an answer
            answer = request.form.get("answer").strip()
            if not answer:
                flash("Please provide an answer before submitting.", "error")
            else:
                try:
                    feedback = bleach.clean(coach.generate_feedback(question, answer))
                    session["answers"][q_index] = answer
                    session["feedbacks"][q_index] = feedback
                except Exception as e:
                    flash(f"Error generating feedback: {str(e)}", "error")
                    feedback = None

        # Navigation buttons
        if "next" in request.form:
            session["q_index"] = min(q_index + 1, len(questions) - 1)
            return redirect(url_for("index"))
        elif "prev" in request.form:
            session["q_index"] = max(q_index - 1, 0)
            return redirect(url_for("index"))

    return render_template(
        "index.html",
        question=question,
        feedback=feedback,
        answer=answer,
        q_index=q_index + 1,
        total=len(questions)
    )

@app.route("/reset")
def reset():
    session.clear()
    flash("Interview session has been reset.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)