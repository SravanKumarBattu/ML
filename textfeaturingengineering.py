# -*- coding: utf-8 -*-
"""TextFeaturingengineering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nF9wyAICS9gHpdZF6AnofwVZeVUMiDVs
"""

import pandas as pd
import numpy as np
import re
import nltk

corpus=[      'the sky is beautiful',
          'love this beautiful blue sky',
          'the fox jumped from the tree',
          'beautiful sky is looking pretty',
          'the dog is lazy as humans',
          'the lion roar is heard from distance'
]
labels=['weather','weather','animal','weather','animal','animal']
corpus=np.array(corpus)
corpus_df=pd.DataFrame({
    'Document': corpus,
    'Category': labels,
})
corpus_df=corpus_df[['Document','Category']]
corpus_df

wpt=nltk.WordPunctTokenizer()
nltk.download('stopwords')
stop_words=nltk.corpus.stopwords.words('english')
def normalize_document(doc):
  doc=re.sub(r'[^a-zA-z0-9\s]','',doc,re.I)
  doc=doc.lower()
  doc=doc.strip()

  tokens=wpt.tokenize(doc)
  filtered_items=[token for token in tokens if token not in stop_words]
  doc=' '.join(filtered_items)
  return doc
normalize_df=np.vectorize(normalize_document)

norm_corpus=normalize_df(corpus)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(min_df=0,max_df=1)
cv_mat=cv.fit_transform(norm_corpus)
cv_mat=cv_mat.toarray()
cv_mat

vocab=cv.get_feature_names()
pd.DataFrame(cv_mat,columns=vocab)

