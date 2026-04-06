# 🤖 AI Chatbot (Flask + OpenAI + MongoDB)

## 📌 Overview
This project is a full-stack AI-powered chatbot built using Python and Flask.  
It allows users to interact through a web interface, generates intelligent responses using an AI API, and stores conversation history in MongoDB.

---

## 🚀 Features
- 💬 Real-time chatbot interaction  
- 🧠 AI-generated responses  
- 💾 Chat history stored in MongoDB  
- 🌐 Web-based UI using Flask  
- ⌨️ Supports Enter key + button input  
- ⏳ Typing indicator (loader)  
- ⚠️ Error handling for API failures  

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MongoDB  
- **API:** OpenAI API  

---

## 📂 Project Structure

AI-Chatbot-Flask/
│
├── app.py
├── templates/
│ └── index.html
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/AI-Chatbot-Flask.git
cd AI-Chatbot-Flask

pip install -r requirements.txt

Set up api key:
setx OPENAI_API_KEY "your_api_key_here"

Make sure MongoDB is running locally:
mongodb://localhost:27017/

Run Application:
python app.py
