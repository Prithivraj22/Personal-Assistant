from sklearn.linear_model import LogisticRegression
import pickle

X = ["hello", "hi", "help", "exit", "what is your name", "who are you"]
y = ["greeting", "greeting", "help", "exit", "identity", "identity"]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

with open('logistic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
