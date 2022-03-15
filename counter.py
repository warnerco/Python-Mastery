#source: https://stackoverflow.com/questions/22094224/how-to-find-total-number-of-positive-and-negative-words-from-a-text/22095243#22095243
from collections import Counter

def readwords(f):
    f = open("thehoundofthebaskervilles.txt")
    words = [ line.rstrip() for line in f.readlines()]
    return words

positive = readwords('positive.txt')
negative = readwords('negative.txt')

story = 'thehoundofthebaskervilles.txt'

count = Counter(story.split())

pos = 0
neg = 0

for key, val in count.iteritems():
    key = key.rstrip('.,?!\n') # removing possible punctuation signs
    if key in positive:
        pos += val
    if key in negative:
        neg += val

print(pos,neg)
