import streamlit as st
from textblob import TextBlob

def get_sentiment_emoji(text):
    """Classifies sentiment and returns corresponding emoji.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The emoji representing the predicted sentiment.
    """

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return "\U0001F600"  # Smiley face emoji
    elif polarity < -0.3:
        return "\U0001F61E"  # Frowning face emoji
    else:
        return "\U0001F610"  # Neutral face emoji

def main():
    """Streamlit app for sentiment emoji analysis with animation."""

    st.title("Sentiment Emoji Analyzer")

    user_input = st.text_input("Enter a sentence:")

    if user_input:
        sentiment_emoji = get_sentiment_emoji(user_input)
        st.write("Your sentence:", user_input)
        st.write("Sentiment:")

        # Display the emoji with animation using st.markdown
        st.markdown(f"<h1 id='sentiment-emoji'>{sentiment_emoji}</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
