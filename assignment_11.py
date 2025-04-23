"""
 Jupyter Notebook is inside case_study_project folder and this file contains streamlit app code
"""

import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from groq import Groq

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

client = Groq(api_key="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")

if "history" not in st.session_state:
    st.session_state.history = []
if "reset" not in st.session_state:
    st.session_state.reset = False

def interpret_emotion(compound_score):
    if compound_score <= -0.5:
        return "Very Sad 😢"
    elif -0.5 < compound_score <= -0.05:
        return "Anxious 😟"
    elif -0.05 < compound_score < 0.05:
        return "Neutral / Uncertain 😐"
    elif 0.05 <= compound_score < 0.5:
        return "Content / Calm 🙂"
    else:
        return "Happy / Uplifted 😊"

def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] >= 0.05:
        sentiment = "POSITIVE"
    elif scores['compound'] <= -0.05:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"
    emotion = interpret_emotion(scores['compound'])
    return sentiment, scores['compound'], emotion

def generate_response(full_history, user_msg, sentiment, score, emotion):
    context = "\n".join([f"User: {h['user']}\nBot: {h['bot']}" for h in full_history])
    prompt = f"""
You are a mental health support assistant. The previous chat history is:
{context}

The user now says: '{user_msg}' and their sentiment is {sentiment} ({score:.2f}) with emotional state: {emotion}.
Respond empathetically.
"""
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
    )
    return completion.choices[0].message.content.strip()

st.set_page_config(page_title="Mental Health Chatbot", layout="centered")
st.title("🧠 Mental Health Chatbot")

if st.button("🔁 Start New Chat"):
    st.session_state.history = []
    st.rerun()

for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Sentiment:** {chat['sentiment']} ({chat['score']:.2f}) — Status: {chat['emotion']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.divider()

user_input = st.text_area("Say something...", height=100, key="user_input")

if st.button("Send"):
    if user_input.strip():
        sentiment, score, emotion = analyze_sentiment(user_input)
        bot_reply = generate_response(st.session_state.history, user_input, sentiment, score, emotion)

        st.session_state.history.append({
            "user": user_input,
            "sentiment": sentiment,
            "score": score,
            "emotion": emotion,
            "bot": bot_reply
        })

        st.rerun()
    else:
        st.warning("Please enter something to send.")
