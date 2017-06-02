def removePunctuation(text):
    import string
    di = {ord(c) : None for c in string.punctuation}
    tab = str.maketrans(di)
    return text.translate(tab)

commonWords = ['the', 'at', 'in', 'to', 'as', 'an', 'a']

def compareStr(str1, str2):
    str1, str2 = removePunctuation(str1), removePunctuation(str2)
    str1_words = str1.split()  # splitting on whitespaces(default action)
    str2_words = str2.split()

    #remove all the commonly occuring words
    str1_words = [word for word in str1_words if word not in commonWords]
    str2_words = [word for word in str1_words if word not in commonWords]

    #now, obtain the "score". Score is the number of words in str1 which are
    #also present in str2 (no penalty for order of words as of now)
    score = 0

    for word in str1_words:
        if word in str2_words:
            score += 1

    return score
