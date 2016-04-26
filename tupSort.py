#The top 10 most common words
fname = raw_input("Enter the file name:")
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key,val in counts.items():
    lst.append((val,key))

lst.sort(reverse=True)

for val,key in lst[:10]:
    print key, val
    