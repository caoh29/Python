import sys


fname = str(input('Enter a file name: '))
try:
    fhandler = open(fname)
except:
    print(f'The file {fname} cannot be opened')
    sys.exit()

def counting_lines():
    global count
    count = 0
    for line in fhandler:
        count = count + 1
    return count

def printing_what_wanted():
    fhandler = open(fname)
    for line in fhandler:
        line = line.strip()
        if keyword not in line:
            continue
        print(line)

def adding_words_to_list():
    fhandler = open(fname)
    for line in fhandler:
        line = line.strip()
        for word in line.split():
            if word not in list:
                list.append(word)

def adding_letters_to_list():
    fhandler = open(fname)
    for line in fhandler:
        line = line.strip()
        for letter in line:
            if letter not in list:
                list.append(letter)

list = []
#keyword = 'pgl'
counting_lines()
print(count)
adding_words_to_list()
list.sort()
print(list)