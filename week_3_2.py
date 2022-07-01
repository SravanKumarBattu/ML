# -*- coding: utf-8 -*-
"""week_3_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fw382imb0O5-AJzuvPslORe1Slxw0ing

##Transforming Nominal Features
"""

import pandas as pd
import numpy as np

vg_df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/vgsales.csv',encoding='utf-8')
vg_df[['Name','Platform','Year','Genre','Publisher']].iloc[1:7]

genres=np.unique(vg_df['Genre'])
genres

from sklearn.preprocessing import LabelEncoder

gle=LabelEncoder()
genre_labels=gle.fit_transform(vg_df['Genre'])
genre_mappings={index: label for index,label in enumerate(gle.classes_)}
genre_mappings

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as spstats

# %matplotlib inline
mpl.style.reload_library()
mpl.style.use('classic')

poke_df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Pokemon.csv',encoding='utf-8')
poke_df.head()

poke_df[['HP','Attack','Defense']].head()

poke_df[['HP','Attack','Defense']].describe()

"""###Counts"""

from sklearn.preprocessing import MinMaxScaler

mmScaler=MinMaxScaler(feature_range=(0,1))

x=poke_df.values[:,0:8]

rescaleX=mmScaler.fit_transform(x)



"""###Natural Lang Tool kit"""

import pandas as pd
import numpy as np
import re
import nltk

corpus=['The sky is blue and beautiful.',
    'Love this blue and beautiful sky.',
    'The quick brown fox jumps over the lazy dog.',
    'The brown fox is quick and the blue dog is lazy.',
    'The sky is very blue and the sky is very beautiful today.',
    'The dog is lazy but the brown fox is quick!']

labels=['weather','weather','animal','animal','weather','animal']
corpus=np.array(corpus)
corpus_df=pd.DataFrame({'Document':corpus, 'Category':labels})
corpus_df=corpus_df[['Document','Category']]
corpus_df

"""##Simple Text-preprocessing"""

nltk.download('stopwords')

wpt=nltk.WordPunctTokenizer()
stop_words=nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    #lowercase and remove special charecters
    doc=re.sub(r'[^a-zA-Z0-9\s]','',doc,re.I)
    doc=doc.lower()
    doc=doc.strip()
    tokens=wpt.tokenize(doc)
    filtered_tokens=[token for token in tokens if token not in stop_words]
    doc=' '.join(filtered_tokens)
    return doc
normalize_corpus=np.vectorize(normalize_document)

norm_corpus=normalize_corpus(corpus)
norm_corpus

"""###Bag of words Model"""

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(min_df=0.,max_df=1.)
cv_matrix=cv.fit_transform(norm_corpus)
cv_matrix=cv_matrix.toarray()
cv_matrix

vocab=cv.get_feature_names()
pd.DataFrame(cv_matrix,columns=vocab)
