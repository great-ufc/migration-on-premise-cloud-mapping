import gensim
from gensim import corpora
import pyLDAvis.gensim_models
import os
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

stop_words.update(list(string.punctuation))

stop_words.update([str(n) for n in range(10)])

stop_words.add('’')
stop_words.add('also')
stop_words.add('would')
stop_words.add('one')
stop_words.add('use')
stop_words.add('”')
stop_words.add('“')
stop_words.add('–')
stop_words.add('sp')
stop_words.add('fig')
stop_words.add('x')
stop_words.add('et')
stop_words.add('c')
stop_words.add('al')
stop_words.add('applications')
stop_words.add('services')
stop_words.add('systems')
stop_words.add('approaches')
stop_words.add('costs')
stop_words.add('servers')
stop_words.add('resources')
stop_words.add('microservices')
stop_words.add('goals')

texts = []

directory = 'artigo/conteudo'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as f:
            text = f.read()
            words = word_tokenize(text)
            texts.append(text)

words = [[word for word in word_tokenize(text.lower()) if word not in stop_words and len(word) > 3 and not word.isdigit()] for text in texts]

dictionary = corpora.Dictionary(words)
corpus = [dictionary.doc2bow(text) for text in words]

lda_model = gensim.models.LdaModel(corpus, num_topics=6, id2word=dictionary, passes=2)

lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(lda_display, 'lda6novotopics.html')