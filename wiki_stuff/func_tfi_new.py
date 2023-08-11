from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import sys
import time

#I'm writing this as a function since it's better overall and it takes forever to run, so it's better to run it in a main
def tf_idf(myfile):

    #The time it took to run it became an interest
    start = time.time()
    np.set_printoptions(threshold=sys.maxsize)
    #myfile is any file really, theoretically wiki_en or wiki_short
    file = open(myfile, 'r')
    #file = open('func_word_list.txt', 'r')
    
    #file2 is the list of the top x words in a file. I have hardcoded it to be this file since func_top_words.py outputs to that file
    file2 = open('func_top_words_out.txt', 'r')
    out = open('Function_Output.txt', 'w')
    #Corpus is the "body" of text we will use later
    corpus = []

    #break the file into an array of the articles in the file
    #I don't know why we use rstrip, I feel it could be done better but I'm not positive so I'm not changing it
    for article in file:
        corpus.append(article.rstrip())

    #this makes a tf_idf Vectorizer object, the pattern determines what it accepts as letters and words
    #I don't like that I can't see where it decides to use corpus, Vectorizer might default to taking something called corpus, but I don't like that I'm not sure
    #Thinh or Sasha used this to get a vocabulary, I think you could do better with a loop that makes a vocab, I don't know how efficient vectorizer(vocab_) is but I feel it must be inefficient
    #I made a function called func_filter or make_unique or something that is a loop through a file which then outputs a vocabulary into a text file, I think that's faster
    tfidf = TfidfVectorizer(token_pattern=r'[a-z]+')
    #This is sorts the vectorizer to get a vocabulary we inted
    word_list = sorted(tfidf.vocabulary_)

    #for every word in the top X words
    #top_words is a dictionary that uses i as a key and its value is a list of its top related words. I believe this list does not get sorted
        #originally top words was outside the loop, but just in case to save on memory we moved it inside the loop, it makes a single key and value before being clearled when i advances
    #top_dot is a dictionary that keeps track of the values with the highest dot products of a given word and i, it is used in making top_words
    #word_pair is a list of the pairs of words we make, see below
    for i in file2:
        top_words = {}
        top_dot = {}
        word_pair = []
    #This will grab the two words
    # i is a word from the top x we want to get relations from, j is every word in the overall vocabulary, we will not make pairs of duplicate words
        for j in range(len(word_list)):
            if i != word_list[j]:
                word_pair.append(i, word_list[j])
        #I wanted to know when it got to the matrix, which I think is the largest time sink
        #its not actually a matrix, its just those two words together
        print("making the 'matrix'")
        for pair in word_pair:
            tfidf_pairs = TfidfVectorizer(token_pattern=r'[a-z]+', vocabulary=pair)
            tfidf_pairs_matrix = tfidf_pairs.fit_transform(corpus)
            dot_product = np.dot(tfidf_pairs_matrix.toarray()[:, 0], tfidf_pairs_matrix.toarray()[:, 1])
            #this part takes the top 10 dot products of all the pairs and puts them into a list, they need to be sorted
            if len(top_dot) < 10:
                top_dot[str(pair)] = dot_product
            else:
                for a in top_dot:
                    if top_dot[a] < dot_product:
                        del top_dot[a]
                        top_dot[str(pair)] = dot_product
                        break
        print("done making the 'matrices'")
        #dot products should be sorted here, its not too hard, just running sorted(reverse=True, key=lambda X;X[:1]) or something like that on the dictionary
        #low is a list of words, it will become the value to a specific key in top_words, it starts empty
        low = []
        for k in top_dot:
            #rather than doing something reasonable, new_string exists so we can tear apart the str(pair) output and collect all the parts we need in a new string
            new_string = ""
            count = 0
            for p in k:
                if p == '\'':
                    count += 1 
                #There were always 3 apostrophes before our word and an apostrophe at the end of it, so counting the apostrophes and only words when 3 of God's commas have been counted works
                elif p != '\'' and p != ' ' and count == 3:
                    new_string = new_string + p
            low.append(new_string)
        top_words[i] = low
        out.write(str(top_words))
        out.write('\n')

    end = time.time() - start
    print("finished the tf_idf after: ")
    print(end)
    ender = "\n Ended after " + end + " seconds."
    out.write(ender)

    #file.close()
    #file1.close()
    file2.close()
    out.close()
