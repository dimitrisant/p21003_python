from urllib.request import Request, urlopen
"""from scipy.stats import entropy as en
import pandas as pd"""
import math


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

data = str(data)
a = data.split(",")
round = a[0][-7:]
round = int(round)
randomness = str(a[1][14:-1])
ath = randomness

for i in range(round-1, round-19, -1):
    link = "https://drand.cloudflare.com/public/" + str(i)
    req2 = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req2).read()
    data = str(data)
    a = data.split(",")
    randomness = str(a[1][14:-1])
    ath += randomness

"""pds = pd.Series(ath)
pds_values = ath.value_counts()
entropy = en(pds_values)"""

def entropy(ath):
    prob = [float(ath.count(i))/len(ath) for i in dict.fromkeys(list(ath))]
    entropy = -sum(x * math.log(x) / math.log(2.0) for x in prob)
    return entropy

en = entropy(ath)
print("Η εντροπία είναι: ", en)
