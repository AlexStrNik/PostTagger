import pickle

import nltk
from nltk.corpus import stopwords
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


n_features = 5000
n_topics = 42
n_top_words = 3

word_bank = pickle.load(open("cleared_wb.pickle", "rb"))

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ,".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


tfidf_vectorizer = TfidfVectorizer(max_df=0.7, max_features=n_features, stop_words=stopwords.words('russian'),
                                   ngram_range=[2, 3])
tfidf_matrix = tfidf_vectorizer.fit_transform(word_bank)

tf_vectorizer = CountVectorizer(max_df=0.7, max_features=n_features, stop_words=stopwords.words('russian'),
                                ngram_range=[2, 3])
tf_matrix = tf_vectorizer.fit_transform(word_bank)

lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=15, learning_method='online',learning_offset=50., random_state=42).fit(tf_matrix)
nmf = NMF(n_components=n_topics, random_state=1, alpha=.1, l1_ratio=.5).fit(tfidf_matrix)

print("\nTopics in NMF model:")
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
print_top_words(nmf, tfidf_feature_names, n_top_words)

print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)
e = {"tf":tf_vectorizer,"lda":lda,"tfidf":tfidf_vectorizer,"nmf":nmf}
pickle.dump(e,open('models.pickle','wb'))