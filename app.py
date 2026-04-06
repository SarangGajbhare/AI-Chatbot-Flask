
from logging import exception
from operator import index

from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from pymongo import MongoClient

app = Flask(__name__)

#API Client
client = OpenAI(api_key="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")

# MongoDB Setup
clientdb = MongoClient("mongodb://localhost:27017/")
db = clientdb["chatbotdb"]
collection = db["messages"]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods = ["POST"])
def chat():
    user_input = request.json.get("message")
    print("User message:", user_input)

    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
            {"role":"system","content":"Your helpful chatbot"},
            {"role":"user","content":user_input}
                        ],
            timeout = 5 # max wait 5 second
        )
        bot_reply = response.choices[0].message.content

    except Exception as e:
        bot_reply = f"Error: {str(e)}"

        if "insufficient_quota" in bot_reply:
            bot_reply = "⚠️ API quota exceeded. Please try later."
        elif "Network error" in bot_reply:
            bot_reply = "Hi! I'm offline right now, but how can I help? 😊"
        else:
            bot_reply = "⚠️ Server error. Try again."

        print("API Error:", bot_reply)

        print("Bot reply:", bot_reply)

        # ✅ ALWAYS SAVE (THIS IS THE FIX)
    result = collection.insert_one({
        "user": user_input,
        "bot": bot_reply
    })

    print("Saved to DB:", result.inserted_id)

    return jsonify({"reply": bot_reply})

@app.route("/history", methods = ["GET"])
def history():
    chats = list(collection.find({}, {"_id":0}))
    return jsonify(chats)

if __name__  == "__main__":
    app.run(debug = True)