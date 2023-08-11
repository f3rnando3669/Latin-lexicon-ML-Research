from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import sys
import time

def tf_idf():

    start = time.time()
    numpy.set_printoptions(threshold=sys.maxsize)
    #file = open(myfile, 'r')
    #file = open('func_word_list.txt', 'r')
    file2 = open('func_top_words_out.txt', 'r')
    out = open('Function_Output.txt', 'w')
    corpus = []

    #break the file into an array of the articles in the file
    for article in file:
        corpus.append(article.rstrip())

    tfidf = TfidfVectorizer(token_pattern=r'[a-z]+')
    #make the bag of words
    word_list = sorted(tfidf.vocabulary_)

    counter = 1
    #for every word in the top ten thousand words
    for i in file2:
        top_words = {}
        top_dot = {}
        word_pair = []
    #This will create the two words.
        for j in range(len(word_list) - counter):
            if i != word_list[j+counter]:
                word_pair.append(i, word_list[j+counter])
        print("making the matrix")
        for pair in word_pair:



    file.close()
    #file1.close()
    file2.close()
    out.close()
