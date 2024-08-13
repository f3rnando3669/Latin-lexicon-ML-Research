import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from sampledataset import get_new_random_data
from Clients.Utilities.FileUtilities import readjson
from heapq import heapify
from classification import prepare_summary_for_bert
from driver_utilities import generate_batch_directory

model = AutoModelForSequenceClassification.from_pretrained("q3fer/distilbert-base-fallacy-classification")
tokenizer = AutoTokenizer.from_pretrained("q3fer/distilbert-base-fallacy-classification")

dataset_path = r'MachineLearningSummer/fallacy_dataset/datasets/30%_of_dataset.csv'
selected_labels = select_labels = {'<IR>', '<FE>', '<RR>', '<G>', '<DEP>', '<FU>', '<WCB>'}
test_list, _ = get_new_random_data(dataset_path, 50, selected=selected_labels)
mappings_path = r'MachineLearningSummer/fallacy_dataset/fallacy_to_abrev.json'
mappings = readjson(mappings_path)
category_correctness = {label:{'Correct':0, 'Total':0} for label in test_list}

for label in test_list:
    for article in test_list[label]:
        inputs = tokenizer(article, return_tensors='pt')

        with torch.no_grad():
            logits = model(**inputs)
            scores = logits[0][0]
            scores = torch.nn.Softmax(dim=0)(scores)
        
        _, ranking = torch.topk(scores, k=scores.shape[0])
        ranking = ranking.tolist()
        results = [(-scores[ranking[i]], model.config.id2label[ranking[i]]) for i in range(scores.shape[0])]
        heapify(results)
        top_score, top_label = results[0]
        mapping = 'other'
        if top_label in mappings:
            mapping = mappings[top_label]
        if mapping == label:
            category_correctness[label]['Correct'] +=1
            category_correctness[label]['Total'] += 1
        else:
            category_correctness[label]['Total'] += 1
        
working_directory = generate_batch_directory()
prepare_summary_for_bert(category_details=category_correctness, batch_dir=working_directory, dataset_path=dataset_path)