import func_top_words as ftw
import func_tf_idf_products as ttt
import sys
import time

file = input("What file should run?")

ftw.top_words(file)
ttt.tf_idf(file)
