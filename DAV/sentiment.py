from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Corrected assignment
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    text = input("Enter the text for sentiment analysis: ")  # Corrected missing parenthesis
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)

if __name__ == "__main__":  # Corrected indentation
    main()  # Corrected indentation