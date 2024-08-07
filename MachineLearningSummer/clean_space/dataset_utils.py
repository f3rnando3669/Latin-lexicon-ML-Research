import pandas as pd

def get_labels(path):
    df = pd.read_csv(path)
    labels = df['label'].loc[::-1]
    return labels

def get_articles(path):
    df = pd.read_csv(path)
    articles = df['article'].loc[::-1]
    return articles

def get_labels_and_articles(path):
    df = pd.read_csv(path)
    labels = df['label'].loc[::-1]
    articles = df['article'].loc[::-1]
    return zip(labels, articles)

def get_limited_labels_and_articles(tags, labels_and_articles, limit=1):
    tag_to_article = {tag:[] for tag in tags}
    for tag, article in labels_and_articles:
        if tag in tags:
            if len(tag_to_article[tag]) == limit:
                continue
            tag_to_article[tag].append(article)
    return tag_to_article