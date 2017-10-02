import pickle

js = []
word_bank = pickle.load(open("cleared_wb.pickle", "rb"))
words=[]
_ = [words.extend(d.split(' ')) for d in word_bank]
words=set(words)
data = pickle.load(open("all_news.pickle","rb"))
for d in data:
    for e in d['text'].split(' '):
        if e not in words:
            js.append(e)
print(set(js))
