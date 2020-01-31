infile = open("text1", 'r')
d = dict()      #initialize a dictionary
for line in infile:
    line = line.lower()         #lower case
    words = line.split()        #split into words
    for word in words:
        if word in d:
            d[word] = d[word] +1
        else:
            d[word] = 1
print(d)
f = open("text1","a")
f.write(str(d))
