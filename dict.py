# Enter a line of text and find the most common word

counts = dict()
line = raw_input("Enter a line of text: ")

words = line.split()
print 'Words: ', words

bigcount = None
bigword = None

for word in words:
    counts[word] = counts.get(word,0) + 1
print " Total count: ",counts

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print 'Common Word: ',bigword,' Count: ',bigcount

print counts.get('hello',-1)