#this text vectoriser implementation uses the hashing trick to find the token string name to feature integer index mapping. (from the documentation)
from sklearn.feature_extraction.text import HashingVectorizer
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)

#text corpus 
corpus = ["It was the best of times",
        "it was the worst of times",
        "it was the age of wisdom",
        "it was the age of foolishness"]

#initialise hashingvectoriser
#features = 7 for 7 words, alternate_sign == False to keep all numbers postive, and no normalisation
hv = HashingVectorizer(n_features=7, alternate_sign=False,norm=None)
#either fit and then transform or using fit_transform work
#fit the corpus and then transform it into the "bag of words like" matrix, but not really
hv.fit(corpus)
train = hv.transform(corpus)
#the numbers mason what do they mean??
print(str(train.toarray()))
