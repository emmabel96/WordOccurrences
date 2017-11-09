__author__ = 'emmabelanger'

from string import punctuation
import csv


from collections import Counter
with open("middle.txt", "wb") as q:

    with open ("s2e12.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                # newWord = re.findall(r'\w+',word)
                newWord = word.strip(punctuation)
                x=''.join(newWord)
                q.write("{}\n".format(x.lower()))
    f.close()
q.close()
with open("s2e12.csv", "wb") as l:
    with open("middle.txt", "r+") as q:
        counts = Counter(q)
        counts.keys()
        w = csv.writer(l)
        for key in counts.items():
            w.writerow(key)




