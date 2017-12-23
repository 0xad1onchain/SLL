from collections import Counter
f = input('Enter file name: ')
fh = open(f)
fre = Counter(fh.read().split());
print("Number of words in the file : \n",fre, "\n")