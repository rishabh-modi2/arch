import os

for a in open('IndiaSpeaks_selftext+perma.txt').read().splitlines():
    f = open('indiaspeaks.html', 'a+')
    f.write('\n    ' + a)