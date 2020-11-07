# enter name of the file
name = input('Enter file name ')
# open the file name / read it
handle = open(name, 'r')
# count the word list and keep it in a dicti
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Prints -> bigword = Prints the most used word in the file
# bigcount = Counts the # of words being used
print(bigword, bigcount)
