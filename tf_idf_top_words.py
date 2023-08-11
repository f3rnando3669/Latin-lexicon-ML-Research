from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)
file = open("wiki_en.txt", "r")
#file1 = open("list_of_tfidf_word_pairs.txt", "w")
file2 = open("Top_Related_Words.txt", "w")
corpus = []
#break wiki_en.txt into an array of all articles
for article in file:
    corpus.append(article.rstrip())

#------------------------------------------------------
tfidf = TfidfVectorizer(token_pattern=r'[a-z]+')
#BOW representation for the documents in the corpus.
tfidf_matrix = tfidf.fit_transform(corpus)
word_list = sorted(tfidf.vocabulary_)
#top_words = {}
#for every word in the vocab
for i in word_list:
    top_words = {}
    top_dot = {}
    word_pair = []
    #create the word pair
    for j in range(len(word_list)-1):
        if i != word_list[j+1]:
            word_pair.append([i, word_list[j+1]])
    #for every pair, build a tfidf matrix with the wiki corpus
    for pair in word_pair:
        tfidf_pairs = TfidfVectorizer(token_pattern=r'[a-z]+', vocabulary=pair)
        tfidf_pairs_matrix = tfidf_pairs.fit_transform(corpus)
        dot_product = numpy.dot(tfidf_pairs_matrix.toarray()[:, 0], tfidf_pairs_matrix.toarray()[:, 1])
        if len(top_dot) < 10:
            top_dot[str(pair)] = dot_product
        else:
            for a in top_dot:
                if top_dot[a] < dot_product:
                    del top_dot[a]
                    top_dot[str(pair)] = dot_product
                    break
    low = []
    for k in top_dot:
        new_string = ""
        count42 = 0
        for p in k:
            if p == '\'':
                count42 = count42 + 1
            elif p != '\'' and p != '[' and p != ' ' and count42 == 3:
                new_string = new_string + p
        low.append(new_string)
    top_words[i] = low
    file2.write(str(top_words))
    file2.write("\n")

#for i in top_words:
#    file2.write(i)
#    file2.write(": ")
#    file2.write(str(top_words[i]))
#    file2.write("\n")
