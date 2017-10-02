import pickle
from DescExtraction import *
import pandas

data = pickle.load(open("bankir_ru_news.pickle","rb"))

for e in data:
    print(e['text'])