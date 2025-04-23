from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Sample data for training
emails = [
    "Get free mоnеу now!",
    "Important meeting tomorrow",
    "Viagra for sale",
    "Meet single moms in your area"
]
labels = [1, 0, 1, 1]  # 1 for spam, 0 for ham

# Feature extraction
vectorizer = CountVectorizer()  # Corrected: Changed '-' to '=' for assignment
X_train_counts = vectorizer.fit_transform(emails)  # Corrected: Changed '-' to '=' for assignment

# Train Naive Bayes classifier
clf = MultinomialNB()  # Corrected: Changed '-' to '=' for assignment
clf.fit(X_train_counts, labels)

# User input
user_input = input("Enter an email: ")  # Corrected: Added closing parenthesis

# Transform user input using the same vectorizer
user_input_counts = vectorizer.transform([user_input])

# Predict
prediction = clf.predict(user_input_counts)

# Output prediction
if prediction[0] == 1:
    print("The email is classified as spam.")
else:
    print("The email is classified as not spam (ham).")