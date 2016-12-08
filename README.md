# average-number-of-words

infile = open('text.txt')

lines = infile.readline()

lines = lines.split(',')

lines = lines.rstrip('\n')

print(lines)

infile.close()
