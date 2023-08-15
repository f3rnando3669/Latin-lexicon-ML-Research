import func_top_words as ftw
import func_tf_idf_products as ttt
import sys
import time

#Given how large wiki_en is and how long all the code together takes, I made this file to run through all the commands needed.
#So each file got turned into a function and here was where they were all supposed to run, taking 'file' as an input so you could give wiki_short or wiki_en

#This code needs to be updated, I think we need more than top_words and tf_idf might be coming from the wrong file.

file = input("What file should run?")

ftw.top_words(file)
ttt.tf_idf(file)
