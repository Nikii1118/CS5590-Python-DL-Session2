from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
# using KNeighbour Classifier
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
#print(tfidf_Vect.vocabulary_)

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train_tfidf,twenty_train.target)


twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = knn.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print(" using KNN Classifier score",score)
# using ngram_range
tfidf_Vect = TfidfVectorizer(ngram_range=(1,2))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
#print(tfidf_Vect.vocabulary_)

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train_tfidf,twenty_train.target)


twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = knn.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print("The new score using bigram",score)
# using stop_word
tfidf_Vect = TfidfVectorizer(stop_words="english")
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
#print(tfidf_Vect.vocabulary_)

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train_tfidf,twenty_train.target)


twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = knn.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print("the score using stop_word",score)

# Using Knn classifier the score is less
#using stop_word accuracy score get increases
