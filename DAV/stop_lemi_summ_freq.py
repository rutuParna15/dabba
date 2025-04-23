#count the frequency of words in a sentence
import nltk
from nltk import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab') # Download the punkt_tab resource
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
word_counts = nltk.FreqDist(tokens)
for word, count in word_counts.items():
  print(f"{word}: {count}") # Changed (word) to {word}


#stemming DAV
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
sentence = input("Enter a WORD: ")
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in sentence.split()]
print("Stemmed words:", stemmed_words)


#lemmatization DAV
import nltk
nltk.download('wordnet')
sentence = input("Enter a word: ")
wn1 = WordNetLemmatizer()
lemmatized_words = [wn1.lemmatize (word) for word in sentence.split()]
print("Lemmatized words:", lemmatized_words)


#identify stop word in a sentence
nltk.download('stopwords')
from nltk.corpus import stopwords
sentence = input("Enter a sentence: ")
tokens = word_tokenize (sentence)
stop_words = stopwords.words('english')
filtered_tokens = [token for token in tokens if token not in stop_words]
print("Filtered tokens:", filtered_tokens)


#INVERSE doc FREQUENCY
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

tfidf = TfidfVectorizer()  # Corrected: Changed '-' to '=' for assignment
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
stop_words = stopwords.words('english')
filtered_tokens = [token for token in tokens if token not in stop_words]
result = tfidf.fit_transform([sentence])  # Corrected: Completed the line and used 'sentence' as input
# If you intended to use filtered tokens, change the above line to:
# result = tfidf.fit_transform([" ".join(filtered_tokens)])
tfidf.vocabulary_
print('\nidf values:')
for elel, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
    print(elel,':', ele2)  # Corrected: Indented the line


import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences):
    """Summarizes text by selecting the top-ranked sentences based on length and stop words."""
    sentences = sent_tokenize(text)
    scores = []
    for sent in sentences:
        word_count = len(sent.split())
        stop_word_count = sum(word in stopwords.words('english') for word in sent.lower().split())
        # Scoring based on length and stop words (customize as needed)
        score = word_count - stop_word_count
        scores.append(score)
    # Sort sentences based on scores and select the top num_sentences
    sorted_sentences = sorted(zip(sentences, scores), key=lambda x: x[1], reverse=True)
    # Extract sentences from sorted tuples and join them for the summary
    summary = " ".join(sent for sent, score in sorted_sentences[:num_sentences])
    return summary

# Example usage
text = "This is a sample test about natural language processing (NLP). NLP is a subfield of artificial Intelligence concerned with the interactions between computers and human Language. It has applications in various fields, including machine translation, tes"
num_sentences = 2
summary = summarize_text(text, num_sentences)
print("Text summary: \n", summary)



