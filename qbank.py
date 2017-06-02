def removePunctuation(text):
    import string
    di = {ord(c) : None for c in string.punctuation}
    tab = str.maketrans(di)
    return text.translate(tab)

def getStopWords():
    with open('minimal_stop.txt') as f:
        stop = f.read().strip()
        stop = stop.split()
        stop = [w for w in stop if w != '']  # remove all blank ones
    return stop

stopWords = getStopWords()

def compareStr(str1, str2):
    str1, str2 = removePunctuation(str1), removePunctuation(str2)
    str1_words = str1.split()  # splitting on whitespaces(default action)
    str2_words = str2.split()

    #covert to lower case
    str1_words = [w.lower() for w in str1_words]
    str2_words = [w.lower() for w in str2_words]

    print("Words after removing punctuations : ")
    print(str1_words)
    print(str2_words)
    print()
    #remove all the commonly occuring words
    str1_words = [word for word in str1_words if word not in stopWords]
    str2_words = [word for word in str2_words if word not in stopWords]
    print("Words after removing stop words : ")
    print(str1_words)
    print(str2_words)
    print()

    #now, obtain the "score". Score is the number of words in str1 which are
    #also present in str2 (no penalty for order of words as of now)
    score = 0

    for word in str1_words:
        if word in str2_words:
            score += 1
    print("Score is : " + str(score))
    return score

compareStr('Explain the need and significance of project report', 'What are the guidelines by planning commission for project report?')
