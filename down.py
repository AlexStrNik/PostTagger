import pickle
import numpy as np

models = pickle.load(open('models.pickle',"rb"))
word_bank = pickle.load(open("cleared_wb.pickle", "rb"))

print(models['lda'].__dict__)
e = models['lda'].transform(models['tf'].transform(word_bank[0:20]))
e2 = models['nmf'].transform(models['tfidf'].transform(word_bank[0:20]))
for topic_idx, topic in enumerate(e):
    print("Topic #%d:" % topic_idx)
    print(" ,".join([models['tf'].get_feature_names()[i] for i in topic.argsort()[:-5 - 1:-1]]))
print()
for topic_idx, topic in enumerate(e2):
    print("Topic #%d:" % topic_idx)
    print(" ,".join([models['tfidf'].get_feature_names()[i] for i in topic.argsort()[:-5 - 1:-1]]))
print()