📄 README.md
# 🤖 AI Interview Coach

An **AI-powered interview coaching web app** built with **Flask** and **Hugging Face Transformers**.  
This project simulates real interview sessions and provides **structured feedback** on answers.

---

## 🚀 Features
- 🎤 **Ask & Answer**: Candidate answers interview questions.
- ✅ **Feedback Structure**:
  - Correct Answer
  - Mistakes
  - Suggestions for Improvement
- 🔄 **Multiple Models**:
  - `google/flan-t5-base` (fast, lightweight)
  - `HuggingFaceH4/zephyr-7b-beta` (chat-style, more detailed)
- 🌐 **Web App Interface** using Flask + HTML templates.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Flask** (backend)
- **Transformers (Hugging Face)** (AI models)
- **Torch** (model support)
- **HTML/CSS** (frontend)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Mhdanshif/AI Interview Coach.git
cd ai-interview-coach

```

2. Create Virtual Environment (Optional but Recommended)
```bah
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```
4. Install Dependencies
```
pip install -r requirements.txt
```
6. Run the App
```
python app.py
```

App will start on: http://127.0.0.1:5000/

## 📦 Requirements

Main dependencies:

- transformers

- torch

- flask

Install all via:
```

pip install -r requirements.txt
```
## 🌍 Deployment

You can deploy this app on:

- Hugging Face Spaces (recommended for ML apps)

- Render or Heroku (Flask hosting)

- Local server

## ✨ Future Improvements

- 🎙️ Add voice input & speech-to-text

- 📊 Analytics dashboard for performance tracking

- 🧑‍🏫 Support for multi-round mock interviews
