# astr = 'Hello Bob'
# istr = 0
# try:
    # istr = int(astr)
# except:
    # istr = -1
    
# print istr
# a = -1.99999999999999999999999999999999999999999
# print type(a)

# big = max('ROVIN NAZARETH')
# small = min('rv')
# print small, big

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends : 
    print 'Happy New Year:',  friend
print 'Done!'

# finding the number in file and then finding the average 
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
avg = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        avg = avg + line[19:].strip()
		count = count + 1
		continue
print "Average spam confidence:",avg/count
