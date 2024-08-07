import pandas as pd
from gensim.models import Word2Vec
import os

csv_path = r'C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\Mo_full_sequence_list.csv'
train_data = pd.read_csv(csv_path)


sequences = [list(seq) for seq in train_data['sequence'].values]

# Train Word2Vec model
word2vec_model = Word2Vec(sequences, vector_size=100, window=5, min_count=1, sg=1, epochs=10)
word2vec_model.save('word2vec.model')