import streamlit as st
from textblob import TextBlob

def get_sentiment_emoji(text):

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return "\U0001F600 \t Happy"  # Smiley face emoji
        # return polarity
    elif polarity <= - 0.3:
        return "\U0001F61E \t Sad"  # Frowning face emoji
        # return 'SAD'
    else:
        return "\U0001F610 \t Neutral"  # Neutral face emoji
        # return polarity

st.title("Sentiment Emoji Analyzer")

user_input = st.text_input("Enter a sentence:")

if user_input:
    sentiment_emoji = get_sentiment_emoji(user_input)
    st.write("Your sentence:", user_input)
    st.write("Sentiment:")

    # Display the emoji with custom styling
    st.markdown(f"<h1 style='text-align:center; font-size:80px;'>{sentiment_emoji}</h1>", unsafe_allow_html=True)
