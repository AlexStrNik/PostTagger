import pickle
import re
import string
from urllib import *
import urllib
from urllib.request import urlopen

import nltk


from bs4 import BeautifulSoup
from nltk.corpus import stopwords


def load_data():
    res=[]
    f = open("arb_news.pickle","rb")
    a = pickle.load(f)
    for e in a:
        if type(e) == dict:
            res.append(e)
    f = open("bankir_ru_news.pickle","rb")
    a = pickle.load(f)
    for e in a:
        if type(e) == dict:
            res.append(e)
    f = open("forbes_news.pickle","rb")
    a = pickle.load(f)
    for e in a:
        if type(e) == dict:
            res.append(e)
    f = open("bosfera.pickle", "rb")
    a = pickle.load(f)
    for e in a:
        if type(e) == dict:
            res.append(e)
    return res
z= []
f = open("bosfera.pickle","rb")
a = pickle.load(f)
for e in a:
    if type(e) == dict:
        z.append(e)
cleared=[]
#stops=[]
#js = ['idDisscus', 'ajax', 'Оценить:', 'voteD', 'fRank', 'поделитьсяподелитьсятвитнутьпечать', 'discuss', 'plus', '„', 'diffVoteRate', 'ПоделитьсяПоделитьсяТвитнутьПечать', 'Комментировать' 'alert', 'voting', 'cmnt', '”', 'mark', 'POST', 'minus', 'if', 'dataType', 'voteDiffRank', 'score', 'type', 'negative', 'return', 'positive', 'data', 'url', 'error', 'jQuery', 'html', '—', 'function', 'success', 'diff', 'json']
#stops.extend(js)
#lstops = [s.lower() for s in stops]
goal = len(z)-1
for d,i in zip(z,range(goal+1)):
    if "text" in list(d.keys()):
        try:
            text=d["text"]

            soup = BeautifulSoup(urlopen(d['link']).read(),"lxml")

            #print(soup)

            text=soup.find("div", attrs={ "class" : "inart" }).get_text()
            #print(text)
            #print('hmmm')
            for e in str("\t\xa0\u200b"):
                text = text.replace(e,' ')
            text = text.strip(' ')
            text = re.sub(' +', ' ', text)
            text = re.sub('\n+', ' ', text)
            text = ' '.join([ e for e in text.split(' ') if e != ' ' and e!='' and e !='\n'])

            d["text"]=text
            cleared.append(d)

        except:
            pass
        print("done " + str(i * 100.0 / goal) + "%")
pickle.dump(cleared,open("bosfera2.pickle","wb"))
print("Done!")