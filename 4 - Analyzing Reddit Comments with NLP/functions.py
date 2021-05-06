import numpy as np
import pickle
import re
import string
import pandas as pd
import spacy
import re
import string
from itertools import cycle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def clean(text):
    '''Removes punctuation, lowercases, removes newlines'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    return text

def pre_clean(documents):
    '''Stores documents in a list after sending each one to cleaning function'''
    cleaned_list = []
    for doc in documents:
        cleaned_list.append(clean(doc))
    return cleaned_list

def lemmatize(text):
    '''Lemmatizes documents and removes stop words'''
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    nlp.max_length = 14082871
    lemmed = []
    for comment in text:
        teckst = nlp(comment)
        lemmed.append(' '.join([word.lemma_ for word in teckst if not word.is_stop]))
    return lemmed

# Create a plot of the PCA results


def plot_PCA_2D(data, target, target_names):
    colors = cycle(['r','g','b','c','m','y','orange','w','aqua','yellow'])
    target_ids = range(len(target_names))
    plt.figure(figsize=(10,10))
    for i, c, label in zip(target_ids, colors, target_names):
        plt.scatter(data[target == i, 0], data[target == i, 1],
                   c=c, label=label, edgecolors='gray')
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")


def vectorize(data, choice='tf_idf', stop_words=None, n_grams=(1,1)):
    if choice == 'tf_idf':
        vectorizer = TfidfVectorizer(stop_words=stop_words, ngram_range=n_grams)
        matrix = vectorizer.fit_transform(data)
        return pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names())
    elif choice == 'cv':
        vectorizer = CountVectorizer(stop_words=stop_words, ngram_range=n_grams)
        matrix = vectorizer.fit_transform(data)
        return pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names())

def display_topics(model, feature_names, no_top_words, topic_names=None):
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

def combine_text(comments):
    combined_text = ' '.join(comments)
    return combined_text
