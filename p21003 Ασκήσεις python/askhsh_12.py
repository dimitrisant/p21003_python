from urllib.request import Request, urlopen
import math

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = str(data)
a = data.split(",")
round = a[0][-7:]
round = int(round)
randomness = a[1][14:-1]
b16 = int(randomness, 16)
k = ''
while b16 > 0:
    k = str(b16 % 2) + k
    b16 = b16 >> 1

b2 = str(k)
ath = b2

for i in range(round-1, round-99, -1):
    link = "https://drand.cloudflare.com/public/" + str(i)
    req2 = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req2).read()
    data = str(data)
    a = data.split(",")
    randomness = a[1][14:-1]
    b16 = int(randomness, 16)
    k = ''
    while b16 > 0:
        k = str(b16 % 2) + k
        b16 = b16 >> 1
    b2 = str(k)
    ath += b2

max0 = max(map(len, ath.split('1')))
max1 = max(map(len, ath.split('0')))
print("Η μεγαλύτερη ακολουθία μηδενικών αποτελείται από: ", max0, " συνεχόμενα μηδενικά")
print("Η μεγαλύτερη ακολουθία μονάδων αποτελείται από: ", max1, " συνεχόμενες μονάδες")
