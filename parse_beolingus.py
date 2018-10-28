import pickle

def read_beolingus(file):
    lines = []
    with open (file, 'rt') as file:
        for line in file:
            line = line.rstrip()
            if not line.startswith('#'):
                lines.append(line)
    return lines

lines = read_beolingus("de-en.txt")



def split_into_german_english(line):
    splitted = line.split('::')
    return splitted

def split_parts(line):
    german = line[0]
    english = line[1]
    germanparts = german.split('|')
    englischparts = english.split('|')
    newParts = {}
    for i, germanpart in enumerate(germanparts):
        newPart = {germanparts[i] : englischparts[i]}
        newParts.update(newPart)
    return newParts


def save_dict(dictonary):
    filename = "newLex"
    with open(filename, 'wb') as picklefile:
        pickle.dump(dictonary, picklefile)
    picklefile.close()

def load_dict():
    new_dict = {}
    with open("newLex", 'rb') as picklefile:
        new_dict = pickle.load(picklefile)
    picklefile.close()
    return new_dict;


dictonary = {}


for i, line in enumerate(lines):
    GermanEnglish = split_into_german_english(line)
    NewParts = split_parts(GermanEnglish)
    part = {i+1 : NewParts}
    dictonary.update(part)

save_dict(dictonary)

new_dict = load_dict()






for k, v in new_dict.items():
    print(k, v)