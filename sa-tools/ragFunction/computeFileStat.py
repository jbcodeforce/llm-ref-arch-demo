import os,codecs


def fileStats(fname):
    with codecs.open(fname,encoding='utf-8',
                 errors='ignore') as infile:
        lines=0
        words=0
        characters=0
        for line in infile:
            wordslist=line.split()
            lines=lines+1
            words=words+len(wordslist)
            characters += sum(len(word) for word in wordslist)
    print("# of lines = " +lines)
    print("# of words = " + words)
    print("# of characters = " + characters)

dirpath="./data"
for (dirpath, dirnames, filenames) in os.walk(dirpath):
    for fnam in filenames:
        fileStats(os.path.join(dirpath,fnam))