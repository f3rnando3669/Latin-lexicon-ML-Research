#bag of words model using sklearn
#credit goes to https://www.kaggle.com/code/vipulgandhi/bag-of-words-model-for-beginners
#package for bag of words model
from sklearn.feature_extraction.text import CountVectorizer
#package or tfidf model
from sklearn.feature_extraction.text import TfidfVectorizer

#example text document (corpus)
#should be in this format
text = ["It was the best of times",
        "it was the worst of times",
        "it was the age of wisdom",
        "it was the age of foolishness"]
# initialise the bag of words model in the BOWvectoriser variable
BOWvectorizer = CountVectorizer()
# tokenize and build vocab
BOWvectorizer.fit(text)
# print out vocab ( all the unique words in the corpus)
print(sorted(BOWvectorizer.vocabulary_))
# BOW representation for the  in the corpus.
BOWvector = BOWvectorizer.transform(text)
# summarize encoded vector
#print(vector.shape)
print(BOWvector.toarray())

#initialise the tf-idf model in the TFIDFvectoriser variable
TFIDFvectorizer = TfidfVectorizer()
# tokenize and build vocab
TFIDFvectorizer.fit(text)
# print out vocab ( all the unique words in the corpus)
print(sorted(TFIDFvectorizer.vocabulary_))
# IDF score for the words in the 4th document in the corpus
TFIDFvector = TFIDFvectorizer.transform([text[3]])
print(TFIDFvectorizer.idf_)

#the IDF score of each word in the vocab relating to its corpus
print(TFIDFvector.toarray())

