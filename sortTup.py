# Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    line.rstrip()
    if not line.startswith('From:') and line.startswith('From'):
        words = line.split()
        hr = words[5]
        hr = hr.split(':')
        for word in hr[:1]:
            counts[word] = counts.get(word,0) + 1
            

lst = list()
for key,val in counts.items():
    lst.append((key,val))

lst.sort()

for key,val in lst:
    print key,val